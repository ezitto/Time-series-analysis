import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
from scipy.fftpack import fft
import io
#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd
import mpld3
#import streamlit as st
from mpld3 import plugins
import streamlit.components.v1 as components
import pywt




# Título de la aplicación
st.title("Análisis de Series Temporales")

# Ingreso de la función matemática
funcion_usuario = st.text_input("Escribe una serie temporal (usa 'np' para funciones de NumPy y 't' como variable):", "np.sin(t)")

# Parámetros para la gráfica
min_t = st.number_input("Valor mínimo de t", value=-5)
max_t= st.number_input("Valor máximo de t", value=10)
step=st.number_input("tiempo muestreo", value=0.01, format="%.6f")

 # Genera un array de valores x
t = np.arange(min_t, max_t, step)
 # Evalúa la función ingresada por el usuario, asegurándose de que usa np.
try:
    y = eval(funcion_usuario)
except Exception as e:
    st.error(f"Error en la función: {e}")
    y = None



#############################################################
        

# Uso de st.session_state para controlar el estado del botón
if 'mostrar_slider' not in st.session_state:
    st.session_state.mostrar_slider = False

# Botón para sumar ruido
if st.button("Sumar ruido"):
    st.session_state.mostrar_slider = True

# Mostrar el slider si el estado es True
if st.session_state.mostrar_slider:
    SNR = st.slider("Relación señal ruido (dB)", min_value=-40, max_value=40, value=0)
    st.write(f"Ruido agregado con SNR de {SNR} dB")

    y_watts = y**2
    y_db = 10 * np.log10(y_watts)
    y_avg_watts = np.mean(y_watts)
    y_avg_db = 10 * np.log10(y_avg_watts)

    noise_avg_db = y_avg_db - SNR
    noise_avg_watts = 10 ** (noise_avg_db / 10)

    mean_noise = 0
    noise_volts = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(y))

    y = y + noise_volts



###############################################################
###############################################################

# Botón para graficar
graficar = st.button("Graficar")

if graficar:
    try:
        # Genera un array de valores x
      #  t = np.arange(min_t, max_t, step)
        # Evalúa la función ingresada por el usuario, asegurándose de que usa np.
       # y = eval(funcion_usuario)
        
        # Crea la gráfica
        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.set_title(f"Gráfica de {funcion_usuario}")
        ax.set_xlabel("t")
        ax.set_ylabel("f(t)")
        
        # Mostrar la gráfica en Streamlit
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error al graficar la función: {e}")
        
        
 ################################################################################
#######################################################################################


# Menú de opciones
opcion = st.selectbox("Selecciona una operación para realizar:", 
                      ("Transformada de Fourier", "Short-Time Fourier Transform (STFT)", "Transformada Wavelet Continua (CWT)", "Calcular derivada", "Calcular integral"))

# Botón para ejecutar la operación
if st.button("Ejecutar análisis"):
    if y is not None:
        if opcion == "Transformada de Fourier":
            
            #fig1, ax = plt.subplots(1, 2, figsize=(10, 4))

           
            # Cálculo de la FFT
            L = len(y)
            Fs = 1 / step
            Y = fft(y)
            P2 = np.abs(Y / L)
            P1 = P2[:L//2+1]
            P1[1:-1] = 2 * P1[1:-1]
            
            # Eje de frecuencias
            f = Fs * np.arange(0, L//2+1) / L
            
            fig1 = plt.figure(figsize=(6,4))
            plt.subplot(121)

            # Gráfico de la señal original
           
            plt.plot(t, y, color='tab:blue') #, marker=',')
            plt.xlabel("t")
            plt.ylabel("X(t)")
            plt.title("Signal")
            
            
            plt.subplot(122)
            
            plt.plot(f, P1, color='tab:orange') #, marker=',')
            plt.xlabel("f (Hz)")
            plt.ylabel("|P1(f)|")
            plt.title("Single-Sided Amplitude Spectrum")
            
            
            # Mostrar la gráfica en Streamlit
            #st.pyplot(fig1)
            #fig_html = mpld3.fig_to_html(two_subplot_fig)
            fig_html = mpld3.fig_to_html(fig1)
            components.html(fig_html, height=400)
            
            
            # Guardar la figura en un archivo en memoria
            buf = io.BytesIO()
            fig1.savefig(buf, format="png")
            buf.seek(0)
            
            # Botón para descargar la imagen
            st.download_button(
                label="Descargar imagen",
                data=buf,
                file_name="grafico_fft.png",
                mime="image/png"
            )
              
             
        ###########
        elif opcion == "Short-Time Fourier Transform (STFT)":
                        # Calcular la STFT (Transformada de Fourier de Tiempo Corto)
        # Calcular la STFT (Transformada de Fourier de Tiempo Corto)
                f, t_stft, Zxx = stft(y, fs=1/step, nperseg=256)
                fig, ax = plt.subplots()
                ax.pcolormesh(t_stft, f, np.abs(Zxx), shading='gouraud')
                ax.set_title("Short-Time Fourier Transform (STFT)")
                ax.set_xlabel("Tiempo [s]")
                ax.set_ylabel("Frecuencia [Hz]")
                st.pyplot(fig)
                        
                        
               
        ###########
        elif opcion == "Transformada Wavelet Continua (CWT)":
           # N = 1000
            #dt = 0.01
            #t = np.linspace(0, N * dt, N)
    
            #f1 = 4
            #s = np.where(t <= 4, 0, np.where(t <= 5, np.sin(2 * np.pi * f1 * t), 0))
    
            fig = plt.figure()
            plt.subplot(2, 1, 1)
            plt.plot(t, y)
    
            escalas = np.arange(2, (max_t-min_t)/step)
            periodos = escalas * step
            frecuencias = 1 / periodos
    
            coefs, _ = pywt.cwt(y, escalas, 'morl')
            frequencies = pywt.scale2frequency('morl', escalas) / step
            c = np.abs(coefs)
    
            plt.subplot(2, 1, 2)
            plt.contourf(t, frequencies, c)
            plt.grid(True)
            st.pyplot(fig)
                                      

                        
        ############
        elif opcion == "Calcular derivada":
                                # Calcular la derivada numérica
                                derivada = np.gradient(y, step)
                                fig, ax = plt.subplots()
                                ax.plot(t, derivada, label="Derivada")
                                ax.set_title(f"Derivada de {funcion_usuario}")
                                ax.set_xlabel("t")
                                ax.set_ylabel("f'(t)")
                                st.pyplot(fig)
                            
        elif opcion == "Calcular integral":
                                # Calcular la integral numérica
                                integral = np.cumsum(y) * step  # Método simple para integrar
                                fig, ax = plt.subplots()
                                ax.plot(t, integral, label="Integral")
                                ax.set_title(f"Integral de {funcion_usuario}")
                                ax.set_xlabel("t")
                                ax.set_ylabel("Integral de f(t)")
                                st.pyplot(fig)
                            
        
        else:
                            st.error("Primero debes definir correctamente una función.")
            
            
