{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PedroNunes-arch/Aula_POO/blob/main/Aula1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "M8lUfl5c3_jf",
        "outputId": "88e07e9a-64e1-462c-851a-ead01c1f0d46"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "invalid decimal literal (1782075229.py, line 11)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_19511/1782075229.py\"\u001b[0;36m, line \u001b[0;32m11\u001b[0m\n\u001b[0;31m    print(f\"Sua media e:\"{media_final:.2f})\u001b[0m\n\u001b[0m                                       ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid decimal literal\n"
          ]
        }
      ],
      "source": [
        "#Projeto de calculo de média\n",
        "class CalculadoraMédia:\n",
        "    def Calculo(self, n1, n2, n3)\n",
        "        return (n1 + n2 + n3) / 3\n",
        "\n",
        "nota1 = input (float(\"Qual a sua primeira nota? \"))\n",
        "nota2 = input (float(\"Qual a sua segunda nota? \"))\n",
        "nota3 = input (float(\"Qual a sua terceira nota? \"))\n",
        "\n",
        "resultado = calc.Calculo(nota1,nota2,nota3)\n",
        "print(f\"Sua media e:\"{media_final:.2f})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sA-OAgWV4PW4"
      },
      "outputs": [],
      "source": [
        "# Projeto de cálculo de média\n",
        "class CalculadoraMedia:\n",
        "    def calcular(self, n1, n2, n3):\n",
        "        return (n1 + n2 + n3) / 3\n",
        "\n",
        "# Criando o objeto da calculadora\n",
        "calc = CalculadoraMedia()\n",
        "\n",
        "# Coletando os dados (convertendo para float)\n",
        "nota1 = float(input(\"Qual a sua primeira nota? \"))\n",
        "nota2 = float(input(\"Qual a sua segunda nota? \"))\n",
        "nota3 = float(input(\"Qual a sua terceira nota? \"))\n",
        "\n",
        "# Chamando a função e exibindo o resultado\n",
        "resultado = calc.calcular(nota1, nota2, nota3)\n",
        "print(f\"A sua média é: {resultado:.2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m4PCdXFM4ztI",
        "outputId": "678541f5-651d-49ef-96bc-243bf31de5ef"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.1/9.1 MB\u001b[0m \u001b[31m1.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m36.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install streamlit -q\n",
        "!pip install pyngrok -q"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dW7gpXXt431W"
      },
      "outputs": [],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "\n",
        "# Customizando o visual\n",
        "st.set_page_config(page_title=\"Calculadora de Média\", page_icon=\"🎓\")\n",
        "\n",
        "st.title(\"🎓 Calculadora de Média Acadêmica\")\n",
        "st.markdown(\"Preencha as notas abaixo para calcular o resultado final.\")\n",
        "\n",
        "# Criando as colunas para as notas\n",
        "col1, col2, col3 = st.columns(3)\n",
        "\n",
        "with col1:\n",
        "    nota1 = st.number_input(\"Nota 1\", min_value=0.0, max_value=10.0, step=0.1)\n",
        "with col2:\n",
        "    nota2 = st.number_input(\"Nota 2\", min_value=0.0, max_value=10.0, step=0.1)\n",
        "with col3:\n",
        "    nota3 = st.number_input(\"Nota 3\", min_value=0.0, max_value=10.0, step=0.1)\n",
        "\n",
        "if st.button(\"Calcular Média Final\", use_container_width=True):\n",
        "    media = (nota1 + nota2 + nota3) / 3\n",
        "\n",
        "    st.divider()\n",
        "    if media >= 6:\n",
        "        st.success(f\"### Parabéns! Sua média foi **{media:.2f}**\")\n",
        "        st.balloons()\n",
        "    elif media >= 5:\n",
        "        st.warning(f\"### Recuperação! Sua média foi **{media:.2f}**\")\n",
        "    else:\n",
        "        st.error(f\"### Reprovado. Sua média foi **{media:.2f}**\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "JtzUtl2e49_w",
        "outputId": "394a2083-f898-4a58-b2b7-91f93becb2c7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Senha para o Tunnel (Password): 35.194.244.76\n",
            "\u001b[1G\u001b[1G\u001b[0K⠙\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠹\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K\u001b[1G\u001b[0JNeed to install the following packages:\n",
            "localtunnel@2.0.2\n",
            "Ok to proceed? (y) \u001b[20G\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K\u001b[1mnpm\u001b[22m \u001b[33mwarn\u001b[39m \u001b[94mexec\u001b[39m The following package was not found and will be installed: localtunnel@2.0.2\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.194.244.76:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0Kyour url is: https://wild-papers-fry.loca.lt\n"
          ]
        }
      ],
      "source": [
        "# Pega o IP público (necessário para o túnel de segurança)\n",
        "import urllib\n",
        "print(\"Senha para o Tunnel (Password):\", urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip())\n",
        "\n",
        "# Inicia o servidor e o túnel\n",
        "!npx localtunnel --port 8501 & streamlit run app.py & npx localtunnel --port 8501"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7PtxzuTO5xUh"
      },
      "outputs": [],
      "source": [
        "!pip install pyngrok -q"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNC3o6h3CIHtxh7iJIpnYiQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}