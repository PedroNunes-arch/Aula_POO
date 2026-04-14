{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOC73b4n3Z1tZUSDSGYK3a+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PedroNunes-arch/Aula_POO/blob/main/Aula_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "collapsed": true,
        "id": "InGRP_udDnVP"
      },
      "outputs": [],
      "source": [
        "def tax_calculator(tx, price):\n",
        "  total = (1+(tx/100))*price\n",
        "  return total"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "value = tax_calculator(20,100)\n",
        "print(value)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_zULtYa0LuMe",
        "outputId": "8c19baf2-8609-4dd8-ffed-a08f27199f8b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "120.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#erro posicional\n",
        "value = tax_calculator(100,20)\n",
        "print(value\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rcgdHvFDMj27",
        "outputId": "72377bb3-9c56-4daf-e860-0a79d8241e46"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "40.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "value = tax_calculator(price=100,tx=20)\n",
        "print(value)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m7jNlV_lNKpm",
        "outputId": "7efb1fad-6695-4d2d-b90f-14f72022db3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "120.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#função com propriedade default\n",
        "def tax_calculator_default(price, tx=20):\n",
        "  total = (1+(tx/100))*price\n",
        "  return f\"O valor {price} adicionado de {tx}% é {total:.2f}\""
      ],
      "metadata": {
        "id": "oCoDCBo0NbUy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response1 = tax_calculator_default(100)\n",
        "print(response1)\n",
        "\n",
        "response2 = tax_calculator_default(100,15)\n",
        "print(response2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EpQECuaXN-i1",
        "outputId": "73fa2ad2-1840-4633-c50d-43514d7c40bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O valor 100 adicionado de 20% é 120.00\n",
            "O valor 100 adicionado de 15% é 115.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ex de função impura\n",
        "#função com propriedade default\n",
        "def tax_calculator_impure(price, tx=20):\n",
        "  total = (1+(tx/100))*price\n",
        "  print(total)\n",
        "  return f\"O valor {price} adicionado de {tx}% é {total:.2f}\""
      ],
      "metadata": {
        "id": "fY4lVqH0PESH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response3 = tax_calculator_impure(100)\n",
        "print(response3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KC3KCleiPcDF",
        "outputId": "dcadf729-6221-4d46-bb24-b6f7e47484f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "120.0\n",
            "O valor 100 adicionado de 20% é 120.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def randomic(number):\n",
        "    result = number + (random.randint(0,10))\n",
        "    return result"
      ],
      "metadata": {
        "id": "csTYUUTwQQ30"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(randomic(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sRnLCcetQpAT",
        "outputId": "088d9798-7620-4f3a-fba4-7e9063b0a493"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ver dps\n",
        "def define_par(number):\n",
        "  if number % 2 == 0:\n",
        "    return f\"{number} é par\"\n",
        "  else:\n",
        "    return f\"{number} é impar\""
      ],
      "metadata": {
        "id": "cUHMzZuTSJOh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(define_par(127))\n",
        "print(define_par(1204))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qk2-66bsSetj",
        "outputId": "4dba5b6e-aa49-4aa0-a19d-3d1e1a7804f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "127 é impar\n",
            "1204 é par\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def area_triangulo(b,h):\n",
        "  area = (b*h)/2\n",
        "  return area"
      ],
      "metadata": {
        "id": "3ahIU2d6TbaL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "base = float(input (\"Digite o valor da base: \"))\n",
        "altura = float(input (\"Digite o valor da base: \"))\n",
        "print(f\" A área do triangulo é: {area_triangulo(base, altura)} u.a.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wc635B92TlAj",
        "outputId": "921b9b24-6ee4-485d-ab79-a30d6bfa6c39"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor da base: 2\n",
            "Digite o valor da base: 3\n",
            " A área do triangulo é: 3.0 u.a.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  base = float(input (\"Digite o valor da base: \"))\n",
        "  altura = float(input (\"Digite o valor da altura: \"))\n",
        "  print(f\" A área do triangulo é: {area_triangulo(base, altura)} u.a.\")\n",
        "\n",
        "except:\n",
        "  print(\"Digite um valor numérico\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EWhcw8nhVaLy",
        "outputId": "2064384f-5972-484e-efd5-908b174d1789"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor da base: 4\n",
            "Digite o valor da altura: 3\n",
            " A área do triangulo é: 6.0 u.a.\n"
          ]
        }
      ]
    }
  ]
}
