{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "str1=\"ABABAB\"\n",
    "str2=\"ABAB\"\n",
    "\n",
    "def longest_gcd(str1: str, str2: str) ->str:\n",
    "    gcd=\"\"\n",
    "    if len(str1)==0 or len(str2)==0:\n",
    "        print(\"GCD of given strings is empty\")\n",
    "    else :\n",
    "        shortest_str = str1 if len(str1) < len(str2) else str2\n",
    "        for i, st in enumerate(shortest_str):\n",
    "            if str1[i] == str2[i]:\n",
    "                gcd[i] = st\n",
    "    return \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mlongest_gcd\u001b[49m\u001b[43m(\u001b[49m\u001b[43mstr1\u001b[49m\u001b[43m,\u001b[49m\u001b[43mstr2\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[1;32mIn[10], line 12\u001b[0m, in \u001b[0;36mlongest_gcd\u001b[1;34m(str1, str2)\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m i, st \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(shortest_str):\n\u001b[0;32m     11\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m str1[i] \u001b[38;5;241m==\u001b[39m str2[i]:\n\u001b[1;32m---> 12\u001b[0m             \u001b[43mgcd\u001b[49m\u001b[43m[\u001b[49m\u001b[43mi\u001b[49m\u001b[43m]\u001b[49m \u001b[38;5;241m=\u001b[39m st\n\u001b[0;32m     13\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "longest_gcd(str1,str2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
