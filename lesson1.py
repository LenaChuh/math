{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "matrix([[ 45. ,  90. ],\n",
       "        [ 63. , 108. ],\n",
       "        [101.7,  45. ],\n",
       "        [225. , 270. ]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "7*np.matrix('5,10;7,12;11.3,5;25,30')+2*np.matrix('5,10;7,12;11.3,5;25,30')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "x=np.linspace(-10,10)\n",
    "for k in [1,3,6]:\n",
    "    plt.figure(figsize=(110,50))\n",
    "    plt.plot(x, np.cos(k*x))\n",
    "    print(x)"
   ]
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
