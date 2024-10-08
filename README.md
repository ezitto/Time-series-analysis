

# Análisis de Series Temporales con Streamlit

Esta es una aplicación interactiva desarrollada con **Streamlit** que permite realizar análisis sobre series temporales mediante transformadas de Fourier, transformadas wavelet, STFT (Transformada de Fourier de Tiempo Corto), así como la posibilidad de agregar ruido y calcular derivadas e integrales de las funciones ingresadas.

## Funcionalidades

- **Ingreso de Función**: El usuario puede ingresar una serie temporal utilizando `NumPy` y `t` como variable.
- **Transformada de Fourier**: Calcula la transformada de Fourier de la serie temporal.
- **Transformada Wavelet Continua (CWT)**: Permite aplicar una transformada wavelet continua sobre la señal.
- **STFT (Short-Time Fourier Transform)**: Realiza la transformada de Fourier en tiempo corto.
- **Ruido a la señal**: Posibilidad de agregar ruido a la señal ingresada controlando la relación señal-ruido (SNR).
- **Cálculo de Derivada e Integral**: Realiza la derivada e integral numérica de la serie temporal.
- **Gráficas Interactivas**: Las gráficas se muestran en tiempo real y se pueden descargar en formato PNG.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación base.
- **Streamlit**: Framework para crear aplicaciones web interactivas.
- **NumPy**: Para el manejo de datos numéricos y la creación de series temporales.
- **Matplotlib**: Para la visualización de datos.
- **SciPy**: Para transformadas de Fourier y otras funciones científicas.
- **PyWavelets**: Para las transformadas wavelet.
- **mpld3**: Para crear gráficas interactivas en HTML.

## Requisitos de Instalación

Para ejecutar esta aplicación localmente, debes tener instalado Python 3.7 o superior y las dependencias del archivo `requirements.txt`.

### Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd tu-repositorio
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## Despliegue en la Nube

Esta aplicación está desplegada en [Streamlit Cloud](https://streamlit.io/cloud). Puedes acceder a ella directamente a través del siguiente enlace:

[**Enlace a la Aplicación**](https://time-series-analysis-uerttn47yneet35phew6ku.streamlit.app/)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar alguna funcionalidad o agregar nuevas características, no dudes en hacer un `fork` del proyecto y enviar un `pull request`.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Puedes ver más detalles en el archivo `LICENSE`.

---

