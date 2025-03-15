{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNDLWA8PeG/hvsRFFXnoQhx",
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
        "<a href=\"https://colab.research.google.com/github/dxzwhite10/Jujun-Munawar_2306148_P3/blob/main/A_star_Search.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from queue import PriorityQueue\n",
        "\n",
        "# Fungsi untuk merekonstruksi jalur dari start ke goal\n",
        "def reconstruct_path(path, start, goal):\n",
        "    current = goal\n",
        "    route = [current]\n",
        "    while current != start:\n",
        "        current = path[current]\n",
        "        route.append(current)\n",
        "    route.reverse()\n",
        "    return route\n",
        "\n",
        "# Fungsi untuk algoritma A* Tree Search\n",
        "def a_star_search(graph, start, goal, heuristic):\n",
        "    frontier = PriorityQueue()  # Antrian prioritas untuk menyimpan simpul yang akan dieksplorasi\n",
        "    frontier.put((0, start))  # Menambahkan simpul awal ke dalam antrian dengan prioritas 0\n",
        "    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi\n",
        "    path = {}  # Dictionary untuk menyimpan jalur\n",
        "    g_cost = {start: 0}  # Menyimpan biaya dari start ke setiap node\n",
        "\n",
        "    while not frontier.empty():\n",
        "        cost_so_far, current_node = frontier.get()  # Mengambil simpul dengan nilai prioritas terendah dari antrian\n",
        "\n",
        "        if current_node == goal:\n",
        "            print(\"Simpul tujuan sudah ditemukan!\")\n",
        "            route = reconstruct_path(path, start, goal)\n",
        "            print(\"Jalur terpendek:\", \" -> \".join(route))\n",
        "            print(\"Total Biaya:\", g_cost[goal])\n",
        "            return True  # Mengembalikan True jika simpul tujuan ditemukan\n",
        "\n",
        "        explored.add(current_node)  # Tandai simpul sebagai telah dieksplorasi\n",
        "\n",
        "        for neighbor, cost in graph.get(current_node, {}).items():\n",
        "            new_g_cost = g_cost[current_node] + cost  # Biaya g(n) = biaya sejauh ini\n",
        "            total_cost = new_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)\n",
        "\n",
        "            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:\n",
        "                frontier.put((total_cost, neighbor))  # Tambahkan ke antrian prioritas\n",
        "                path[neighbor] = current_node  # Simpan jalur yang diambil\n",
        "                g_cost[neighbor] = new_g_cost  # Perbarui biaya jalur sejauh ini\n",
        "\n",
        "    print(\"Simpul tujuan tidak ditemukan!\")\n",
        "    return False  # Jika tidak menemukan tujuan\n",
        "\n",
        "# Daftar heuristik untuk setiap simpul\n",
        "heuristic = {\n",
        "    'S': 6,\n",
        "    'A': 4,\n",
        "    'B': 3,\n",
        "    'C': 3,\n",
        "    'D': 1,\n",
        "    'G': 0\n",
        "}\n",
        "\n",
        "# Graf berbobot (dalam bentuk adjacency list)\n",
        "graph = {\n",
        "    'S': {'A': 3, 'B': 2},\n",
        "    'A': {'D': 5, 'B': 1},\n",
        "    'B': {'C': 2, 'D': 3},\n",
        "    'C': {'G': 4, 'D': 3},\n",
        "    'D': {'G': 1},\n",
        "}\n",
        "\n",
        "# Titik awal dan tujuan\n",
        "start_node = 'S'\n",
        "goal_node = 'G'\n",
        "\n",
        "# Panggil fungsi a_star_search\n",
        "a_star_search(graph, start_node, goal_node, heuristic)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VkoR0KcfnDEq",
        "outputId": "d3bff63d-d385-4395-b301-25a82d3b9071"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Simpul tujuan sudah ditemukan!\n",
            "Jalur terpendek: S -> B -> D -> G\n",
            "Total Biaya: 6\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    }
  ]
}