{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PrabaKDataScience/DeepLearning/blob/main/NLP/Basics/05_stop_words.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b17f58fa",
      "metadata": {
        "id": "b17f58fa"
      },
      "source": [
        "###                     **Stop Words: Exercise**"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "23a26def",
      "metadata": {
        "id": "23a26def"
      },
      "source": [
        "- **Run this cell to import all necessary packages**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "id": "34f02550",
      "metadata": {
        "id": "34f02550"
      },
      "outputs": [],
      "source": [
        "#import spacy and load the model\n",
        "\n",
        "import spacy\n",
        "nlp = spacy.load(\"en_core_web_sm\")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "0fe230d8",
      "metadata": {
        "id": "0fe230d8"
      },
      "source": [
        "**Exercise1:** \n",
        "- From a Given Text, Count the number of stop words in it.\n",
        "- Print the percentage of stop word tokens compared to all tokens in a given text."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "id": "646c9e7a",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "646c9e7a",
        "outputId": "17fbdbd8-c668-4dd1-c62a-ef00f446a3a7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "40\n",
            "25.0\n"
          ]
        }
      ],
      "source": [
        "text = '''\n",
        "Thor: Love and Thunder is a 2022 American superhero film based on Marvel Comics featuring the character Thor, produced by Marvel Studios and \n",
        "distributed by Walt Disney Studios Motion Pictures. It is the sequel to Thor: Ragnarok (2017) and the 29th film in the Marvel Cinematic Universe (MCU).\n",
        "The film is directed by Taika Waititi, who co-wrote the script with Jennifer Kaytin Robinson, and stars Chris Hemsworth as Thor alongside Christian Bale, Tessa Thompson,\n",
        "Jaimie Alexander, Waititi, Russell Crowe, and Natalie Portman. In the film, Thor attempts to find inner peace, but must return to action and recruit Valkyrie (Thompson),\n",
        "Korg (Waititi), and Jane Foster (Portman)—who is now the Mighty Thor—to stop Gorr the God Butcher (Bale) from eliminating all gods.\n",
        "'''\n",
        "\n",
        "#step1: Create the object 'doc' for the given text using nlp()\n",
        "\n",
        "doc = nlp(text)\n",
        "\n",
        "#step2: define the variables to keep track of stopwords count and total words count\n",
        "\n",
        "all_words = 0\n",
        "stop_words =[]\n",
        "\n",
        "#step3: iterate through all the words in the document\n",
        "\n",
        "for token in doc:\n",
        "  all_words+=1\n",
        "  if token.is_stop:\n",
        "    stop_words.append(token.text)\n",
        "  \n",
        "\n",
        "#step4: print the count of stop words\n",
        "\n",
        "print(len(stop_words))    \n",
        "\n",
        "#step5: print the percentage of stop words compared to total words in the text\n",
        "print((len(stop_words)/all_words)*100)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "vsJaC5a-ldY-",
      "metadata": {
        "id": "vsJaC5a-ldY-"
      },
      "source": [
        "**Exercise2:** \n",
        "\n",
        "- Spacy default implementation considers **\"not\"** as a stop word. But in some scenarios removing 'not' will completely change the meaning of the statement/text. For Example, consider these two statements:\n",
        "\n",
        "      - this is a good movie       ----> Positive Statement\n",
        "      - this is not a good movie   ----> Negative Statement\n",
        "\n",
        "- So, after applying stopwords to those 2 texts, both will return **\"good movie\"** and does not respect the polarity/sentiments of text.\n",
        "  \n",
        "- Now, your task is to remove this stop word **\"not\"** in spaCy and help in distinguishing the texts.\n",
        "\n",
        "\n",
        "- **Hint:** GOOGLE IT! Google is your friend.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "id": "4e9e663a",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4e9e663a",
        "outputId": "df09fbcc-e82c-4aeb-f988-e8bf7cfd553d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'was', 'whereupon', 'other', 'eight', 'below', \"'ve\", 'nevertheless', 'five', 'nine', 'two', '’s', '‘ve', 'sometimes', 'n’t', \"'re\", 'hereby', 'amount', 'must', 'name', 'yourself', 'even', 'through', 'whenever', 'whom', 'then', 'me', 'your', 'now', 'along', 'above', 'get', 're', 'most', 'nor', 'three', 'show', 'until', 'a', 'some', 'at', 'really', 'four', 'is', '’d', 'too', '‘s', 'he', 'by', 'up', 'used', 'no', 'per', 'moreover', 'had', 'which', 'often', 'empty', 'others', \"'ll\", \"'m\", 'n‘t', 'whereas', 'yours', 'either', 'hundred', 'almost', 'this', 'are', 'has', 'am', 'those', 'about', 'enough', 'could', 'somehow', 'or', 'another', 'ours', 'someone', 'hereafter', 'from', 'who', 'anyhow', 'latterly', 'thru', 'becoming', 'front', 'fifteen', 'its', 'thus', 'as', 'call', 'each', 'off', 'around', 'give', 'only', 'anyone', 'hers', 'why', 'more', 'move', 'twelve', 'myself', 'thereby', 'whether', 'thence', 'back', 'where', 'become', 'wherever', 'third', 'everywhere', 'between', 'it', 'on', 'never', 'seemed', 'much', 'something', 'thereafter', 'and', 'somewhere', 'make', 'doing', \"'d\", 'there', 'our', 'sometime', 'under', 'forty', 'itself', 'nothing', 'that', 'whose', 'since', '‘re', 'when', '’ve', 'though', 'whereafter', 'whoever', 'once', 'all', 'in', 'did', 'over', 'yourselves', 'ever', 'neither', 'mine', 'former', 'how', 'less', 'so', 'via', 'becomes', 'latter', 'toward', 'upon', 'sixty', 'full', 'nobody', 'these', 'her', \"'s\", 'please', 'wherein', 'such', 'hereupon', 'you', 'but', 'also', 'anywhere', \"n't\", 'many', 'anything', 'for', 'what', 'perhaps', 'with', 'own', 'were', 'least', 'noone', 'anyway', 'mostly', 'seem', 'here', 'beforehand', 'twenty', 'because', 'down', 'ten', 'due', 'be', 'although', 'however', 'beyond', 'namely', 'few', 'side', 'beside', 'everything', 'formerly', 'herself', 'of', 'put', '‘m', 'been', 'every', 'themselves', 'done', 'behind', 'indeed', 'i', 'whither', 'various', '‘ll', 'into', 'made', 'whence', 'six', 'does', 'should', 'an', 'himself', 'again', 'any', 'first', 'to', 'cannot', 'do', 'out', 'within', 'alone', 'further', 'ca', 'part', 'well', 'elsewhere', 'whole', 'ourselves', 'none', 'whereby', 'next', 'always', 'very', 'us', 'while', 'last', 'still', 'bottom', 'if', 'both', 'unless', 'go', 'everyone', 'have', 'hence', 'onto', 'being', 'my', 'they', 'whatever', 'eleven', 'rather', '’re', 'quite', 'top', 'than', '’ll', 'across', 'throughout', 'except', 'already', 'therefore', 'towards', 'can', 'several', 'them', '‘d', 'herein', 'same', 'after', 'would', 'against', 'one', 'serious', 'thereupon', 'nowhere', 'therein', 'before', 'else', 'might', 'take', 'his', 'besides', 'keep', 'amongst', 'without', 'seeming', 'meanwhile', 'may', 'say', 'yet', 'regarding', 'during', 'him', 'became', '’m', 'using', 'afterwards', 'see', 'seems', 'their', 'the', 'among', 'will', 'we', 'otherwise', 'fifty', 'just', 'together', 'she'}\n",
            "good movie\n",
            "not good movie\n"
          ]
        }
      ],
      "source": [
        "#use this pre-processing function to pass the text and to remove all the stop words and finally get the cleaned form\n",
        "def preprocess(text):\n",
        "    doc = nlp2(text)\n",
        "    no_stop_words = [token.text for token in doc if not token.is_stop]\n",
        "    return \" \".join(no_stop_words)       \n",
        "\n",
        "\n",
        "#Step1: remove the stopword 'not' in spacy\n",
        "nlp2 = spacy.load('en_core_web_sm')\n",
        "print(nlp2.Defaults.stop_words)\n",
        "\n",
        "#step2: send the two texts given above into the pre-process function and store the transformed texts\n",
        "\n",
        "res_1 = preprocess('this is a good movie')\n",
        "res_2 = preprocess('this is not a good movie')\n",
        "\n",
        "#step3: finally print those 2 transformed texts\n",
        "print(res_1 , res_2, sep='\\n')"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "RWnHxZy-Fv5S",
      "metadata": {
        "id": "RWnHxZy-Fv5S"
      },
      "source": [
        "**Exercise3:** \n",
        "\n",
        "- From a given text, output the **most frequently** used token after removing all the stop word tokens and punctuations in it. \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "id": "GfLMTZmBFlPI",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GfLMTZmBFlPI",
        "outputId": "de14130f-1af5-470e-db09-0734ea5a37d5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "India 6\n",
            "{'status': 2, 'cricket': 5, 'International': 3, 'ODI': 1, 'T20I': 1, 'sixth': 1, 'team': 3, 'India': 6, 'Men': 1, 'test': 1, 'Blue': 1, 'governed': 1, 'international': 1, 'Test': 2, 'club': 1, ' ': 1, 'introduced': 1, 'Team': 1, '18th': 1, 'Control': 1, 'ICC': 1, '\\n': 5, 'century': 1, 'Cricket': 3, 'Council': 1, 'played': 1, 'Twenty20': 1, 'men': 2, 'Board': 1, '1932': 1, 'June': 1, '1792': 1, '25': 1, 'national': 2, 'British': 1, 'sailors': 1, 'granted': 1, 'established': 1, 'represents': 1, 'BCCI': 1, 'Lord': 1, 'known': 1, 'Member': 1, 'Day': 1, 'match': 1}\n"
          ]
        }
      ],
      "source": [
        "text = ''' The India men's national cricket team, also known as Team India or the Men in Blue, represents India in men's international cricket.\n",
        "It is governed by the Board of Control for Cricket in India (BCCI), and is a Full Member of the International Cricket Council (ICC) with Test,\n",
        "One Day International (ODI) and Twenty20 International (T20I) status. Cricket was introduced to India by British sailors in the 18th century, and the \n",
        "first cricket club was established in 1792. India's national cricket team played its first Test match on 25 June 1932 at Lord's, becoming the sixth team to be\n",
        "granted test cricket status.\n",
        "'''\n",
        "\n",
        "\n",
        "#step1: Create the object 'doc' for the given text using nlp()\n",
        "import spacy \n",
        "nlp = spacy.load('en_core_web_sm')\n",
        "doc = nlp(text)\n",
        "\n",
        "#step2: remove all the stop words and punctuations and store all the remaining tokens in a new list\n",
        "\n",
        "temp_list = [token.text for token in doc if not (token.is_punct or token.is_stop)]\n",
        "\n",
        "#step3: create a new dictionary and get the frequency of words by iterating through the list which contains stored tokens  \n",
        "\n",
        "temp_set =set(temp_list)\n",
        "temp_dict = {}\n",
        "for each in temp_set:\n",
        "  count = temp_list.count(each)\n",
        "  temp_dict[each]=count\n",
        "\n",
        "#step4: get the maximum frequency word\n",
        "max_frequency = max(temp_dict.values())\n",
        "for k, v in temp_dict.items():\n",
        "  if v==max_frequency:\n",
        "    print(k , v)\n",
        "\n",
        "#step5: finally print the result\n",
        "print(temp_dict)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "stop_words_exercise_solutions.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.10"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}