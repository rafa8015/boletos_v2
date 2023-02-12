{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "ebf2fc0c",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "navegador = webdriver.Chrome()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b3cf182f",
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador.get(\"https://auth.netcombo.com.br/web/login.html?client_id=MINHA_CLARO_RESIDENCIAL&redirect_uri=https%3A%2F%2Fminhaclaroresidencial.claro.com.br%2Flogin&response_type=code&scope=openid+minha_net&authMs=UP,EP,DOCP,OTP\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "86b327d5",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "\n",
    "navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/section/div/div[2]/div[1]/div/form/div[1]/div/input').send_keys(\"10406738807\") \n",
    "navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/section/div/div[2]/div[1]/div/form/div[3]/button').click()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "d0ee616b",
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador.find_element(By.XPATH, '//*[@id=\"password\"]').send_keys(\"Rafael159357\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "6ffd05de",
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador.find_element(By.XPATH, '//*[@id=\"FormLogin\"]/div[3]/button').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "95a1fcff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<selenium.webdriver.remote.webelement.WebElement (session=\"cdc6431e9f6956b4de7000276e0f71ff\", element=\"1606bf16-2000-46a6-aed4-2d7070df8e0f\")>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "\n",
    "WebDriverWait(navegador, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"mcr-list-radio-157427817\"]')))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "af5d8efb",
   "metadata": {},
   "outputs": [],
   "source": [
    "botao = navegador.find_element(By.XPATH, '//*[@id=\"mcr-list-radio-157427817\"]')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "5b815b84",
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador.execute_script(\"arguments[0].click();\", botao)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "4684d3c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<selenium.webdriver.remote.webelement.WebElement (session=\"cdc6431e9f6956b4de7000276e0f71ff\", element=\"1eb163a3-6897-4546-a3cd-3797b8061a86\")>"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"app\"]/article/div/div[2]/div/div[3]/button')))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "8b5266cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "botao1 = navegador.find_element(By.XPATH, '//*[@id=\"app\"]/article/div/div[2]/div/div[3]/button')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "652a5c91",
   "metadata": {},
   "outputs": [],
   "source": [
    "navegador.execute_script(\"arguments[0].click();\", botao1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "1733412f",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    botao2 = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"consentimento-lgpd\"]/div/div/div[1]/button'))    )\n",
    "    botao2.click()\n",
    "    botao2 = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"consentimento-lgpd\"]/div/div/div[1]/button'))    )\n",
    "    botao2.click()\n",
    "\n",
    "except:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "4fadf311",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\".mdn-Heading mdn-Heading--xl mdn-u-marginTop--md mdn-u-marginBottom--md\"}\n  (Session info: chrome=109.0.5414.121)\nStacktrace:\nBacktrace:\n\t(No symbol) [0x01196643]\n\t(No symbol) [0x0112BE21]\n\t(No symbol) [0x0102DA9D]\n\t(No symbol) [0x01061342]\n\t(No symbol) [0x0106147B]\n\t(No symbol) [0x01098DC2]\n\t(No symbol) [0x0107FDC4]\n\t(No symbol) [0x01096B09]\n\t(No symbol) [0x0107FB76]\n\t(No symbol) [0x010549C1]\n\t(No symbol) [0x01055E5D]\n\tGetHandleVerifier [0x0140A142+2497106]\n\tGetHandleVerifier [0x014385D3+2686691]\n\tGetHandleVerifier [0x0143BB9C+2700460]\n\tGetHandleVerifier [0x01243B10+635936]\n\t(No symbol) [0x01134A1F]\n\t(No symbol) [0x0113A418]\n\t(No symbol) [0x0113A505]\n\t(No symbol) [0x0114508B]\n\tBaseThreadInitThunk [0x760B6BD9+25]\n\tRtlGetFullPathName_UEx [0x770F8FD2+1218]\n\tRtlGetFullPathName_UEx [0x770F8F9D+1165]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_15800\\1062341627.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mValorClaro\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnavegador\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"mdn-Heading mdn-Heading--xl mdn-u-marginTop--md mdn-u-marginBottom--md\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mValorClaro\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;34m'print(1)'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;34m'print(ValorClaro)'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;34m'print(2)'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m    828\u001b[0m             \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mf'[name=\"{value}\"]'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    829\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 830\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mFIND_ELEMENT\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m\"using\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"value\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"value\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    831\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    832\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_elements\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mID\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mOptional\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[0mList\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mWebElement\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    438\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    439\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 440\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    441\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"value\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"value\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    442\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    243\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"alert\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"text\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    244\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 245\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\".mdn-Heading mdn-Heading--xl mdn-u-marginTop--md mdn-u-marginBottom--md\"}\n  (Session info: chrome=109.0.5414.121)\nStacktrace:\nBacktrace:\n\t(No symbol) [0x01196643]\n\t(No symbol) [0x0112BE21]\n\t(No symbol) [0x0102DA9D]\n\t(No symbol) [0x01061342]\n\t(No symbol) [0x0106147B]\n\t(No symbol) [0x01098DC2]\n\t(No symbol) [0x0107FDC4]\n\t(No symbol) [0x01096B09]\n\t(No symbol) [0x0107FB76]\n\t(No symbol) [0x010549C1]\n\t(No symbol) [0x01055E5D]\n\tGetHandleVerifier [0x0140A142+2497106]\n\tGetHandleVerifier [0x014385D3+2686691]\n\tGetHandleVerifier [0x0143BB9C+2700460]\n\tGetHandleVerifier [0x01243B10+635936]\n\t(No symbol) [0x01134A1F]\n\t(No symbol) [0x0113A418]\n\t(No symbol) [0x0113A505]\n\t(No symbol) [0x0114508B]\n\tBaseThreadInitThunk [0x760B6BD9+25]\n\tRtlGetFullPathName_UEx [0x770F8FD2+1218]\n\tRtlGetFullPathName_UEx [0x770F8F9D+1165]\n"
     ]
    }
   ],
   "source": [
    "ValorClaro = navegador.find_element(By.CLASS_NAME, \"mdn-Heading mdn-Heading--xl mdn-u-marginTop--md mdn-u-marginBottom--md\")\n",
    "\n",
    "print(ValorClaro.text)\n",
    "'print(1)'\n",
    "'print(ValorClaro)'\n",
    "'print(2)'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "cea8b344",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ValorClaro = ValorClaro.text'"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''ValorClaro = ValorClaro.text'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "a31bf61d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'print(ValorClaro)'"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''print(ValorClaro)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca36a5a7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
