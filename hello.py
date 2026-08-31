{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM1rcOpIxqpZBxaVIOZ7GH1",
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
        "<a href=\"https://colab.research.google.com/github/jmyoung-76/jangan-project/blob/main/hello.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jRSxgh_cf4BS",
        "outputId": "184c558d-0676-4643-fac9-741167a4ebfa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: destination path 'jangan-project' already exists and is not an empty directory.\n"
          ]
        }
      ],
      "source": [
        "!git clone https://github.com/jmyoung-76/jangan-project.git\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%run hello.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "KdL9pybCg-Gs",
        "outputId": "0bf46c73-f708-4397-a096-17f8817350c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "Exception",
          "evalue": "File `'hello.py'` not found.",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.13/dist-packages/IPython/core/magics/execution.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, parameter_s, runner, file_finder)\u001b[0m\n\u001b[1;32m    713\u001b[0m             \u001b[0mfpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0marg_lst\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 714\u001b[0;31m             \u001b[0mfilename\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfile_finder\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    715\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.13/dist-packages/IPython/utils/path.py\u001b[0m in \u001b[0;36mget_py_filename\u001b[0;34m(name, force_win32)\u001b[0m\n\u001b[1;32m    108\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 109\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mIOError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'File `%r` not found.'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    110\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOSError\u001b[0m: File `'hello.py'` not found.",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mException\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_2254/2281136686.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun_line_magic\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'run'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'hello.py'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.13/dist-packages/IPython/core/interactiveshell.py\u001b[0m in \u001b[0;36mrun_line_magic\u001b[0;34m(self, magic_name, line, _stack_depth)\u001b[0m\n\u001b[1;32m   2416\u001b[0m                 \u001b[0mkwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'local_ns'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_local_scope\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstack_depth\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2417\u001b[0m             \u001b[0;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbuiltin_trap\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2418\u001b[0;31m                 \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2419\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2420\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<decorator-gen-52>\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, parameter_s, runner, file_finder)\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.13/dist-packages/IPython/core/magic.py\u001b[0m in \u001b[0;36m<lambda>\u001b[0;34m(f, *a, **k)\u001b[0m\n\u001b[1;32m    185\u001b[0m     \u001b[0;31m# but it's overkill for just that one bit of state.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    186\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mmagic_deco\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 187\u001b[0;31m         \u001b[0mcall\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mlambda\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    188\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    189\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mcallable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.13/dist-packages/IPython/core/magics/execution.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, parameter_s, runner, file_finder)\u001b[0m\n\u001b[1;32m    723\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'nt'\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmatch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr\"^'.*'$\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mfpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    724\u001b[0m                 \u001b[0mwarn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'For Windows, use double quotes to wrap a filename: %run \"mypath\\\\myfile.py\"'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 725\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    726\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    727\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mfpath\u001b[0m \u001b[0;32min\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmeta_path\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mException\u001b[0m: File `'hello.py'` not found."
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/jmyoung-76/jangan-project.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jghacEAOhZjW",
        "outputId": "bb6f11b4-91f4-44fd-b59b-daf6e90270c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: destination path 'jangan-project' already exists and is not an empty directory.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%run jangan-project/hello.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WAL1GHQKhmC6",
        "outputId": "d02b5fcb-5a9d-4871-854f-a3220745692a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello git\n",
            "2 - hi jangan\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/jmyoung-76/jangan-project.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CizBPCPPjikf",
        "outputId": "fb9b6412-4a26-4f36-f7e9-3c85de828a97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: destination path 'jangan-project' already exists and is not an empty directory.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8ChoV35ektRs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%cd jangan-project\n",
        "!git pull"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X2FxbLPMkti5",
        "outputId": "b49d6b0e-5e3e-4af4-cc33-3c956294206e"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[Errno 2] No such file or directory: 'jangan-project'\n",
            "/content/jangan-project\n",
            "Updating bbba245..7c721e0\n",
            "error: Your local changes to the following files would be overwritten by merge:\n",
            "\thello.py\n",
            "Please commit your changes or stash them before you merge.\n",
            "Aborting\n"
          ]
        }
      ]
    }
  ]
}