import numpy as np
import requests
from urlparse import urlparse
from numpy.linalg import matrix_power
# import requests_html

# a = np.matrix('1 2; 3 4; 5 6')
# N = a.shape[0]

# print np.matrix('1 2; 3 4; 5 6') +  np.matrix('1 2; 3 4; 5 6')


# # for c in a.T:
# #     rows = c.A[0]
# #     print [row / 3.0 for row in rows]

# x1 = np.arange(9.0).reshape((3, 3))
# print x1
# x2 = np.arange(3.0)
# print np.multiply(x1, 3.0)
# # array([[  0.,   1.,   4.],
# #        [  0.,   4.,  10.],
# #        [  0.,   7.,  16.]])

# i = np.array([[0, 1], [-1, 0]])
# print matrix_power(i, 3)
# print np.ones((3, 3))
# print np.matmul([[0, 1, 1], [0, 0, 1], [1, 0, 0]], [1, 0, 0])
import BeautifulSoup


response = requests.get('http://www.berkeley.edu/')
soup = BeautifulSoup.BeautifulSoup(response.text)
print [urlparse(link.get("href"))[1] for link in soup.findAll("link")]

# print response.text


# session = requests_html.HTMLSession()
# response = session.get('http://www.ftb.ca.gov/')


# html = requests_html.HTML(html=response.text)
# print (html.links)

# d = { "a": "pepe", "b": "popo" }
# for key, value in d.iteritems():
#     print key, value


# matrix = np.zeros([3, 3])
# matrix[1][1] = 2

# print matrix

# def divide_chunks(l, n):      
#     for i in range(0, len(l), n):  
#         yield l[i:i + n] 

# print list(divide_chunks([1, 2, 3, 4, 5], 2))

link = "http://www.berkeley.edu/"

print urlparse(link)
print urlparse(link)[1]
print urlparse(link)[2]
