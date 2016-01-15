#!/usr/bin/env python
#coding: utf8
import operator
import sys
import re
import os
'''Trie树实现字符串数组字典排序'''
class Trie(object):
 def __init__(self):
  self.root  = Node() # Trie树root节点引用
 def add(self, word):
  '''添加字符串'''
  node = self.root
  for i in range(0,len(word),3):
   c=word[i:i+3]
   pos = self.find(node, c)
   if pos < 0:
    node.childs.append(Node(c))
    #为了图简单，这里直接使用Python内置的sorted来排序
    #pos有问题，因为sort之后的pos会变掉,所以需要再次find来获取真实的pos
    #自定义单字符数组的排序方式可以实现任意规则的字符串数组的排序
    node.childs = sorted(node.childs, key=lambda child: child.c)
    pos = self.find(node, c)
   node = node.childs[pos]
  node.word = word
 def preOrder(self, node):
  '''先序输出'''
  results = []
  if node.word:
   results.append(node.word)
  for child in node.childs:
   results.extend(self.preOrder(child))
  return results
 def find(self, node, c):
  '''查找字符插入的位置'''
  childs = node.childs
  _len   = len(childs)
  if _len == 0:
   return -1
  for i in range(_len):
   if childs[i].c == c:
    return i
  return -1
 def setWords(self, words):
  for word in words:
   self.add(word)
 def findWords(self,word):
 	nodetemp=self.root
 	lenword = len(word)
 	for ind in range(0,lenword,3):
 		key=word[ind:ind+3]
 		#print nodetemp.c,key,nodetemp.word,nodetemp.childs[0].c
 		pos=self.find(nodetemp,key)
 		if pos>=0:
 			nodetemp = nodetemp.childs[pos]
 			if word == nodetemp.word:
 				return True
 	return False

class Node(object):
 def __init__(self, c=None, word=None):
  self.c          = c    # 节点存储的单个字符
  self.word       = word # 节点存储的词
  self.childs     = []   # 此节点的子节点
  self.finished   = 0    # 此节点是一个合法值的终止节点
if __name__ == '__main__':
#	pass
 words = ['北京', '上海', '石家庄', '北京北', '上海南']
 trie = Trie()
 trie.setWords(words)
 trie.add("阳光人寿保险")
 result = trie.preOrder(trie.root)
 print '原始字符串数组: [' + ', '.join(words) + ']'
 print 'Trie树排序后: [' + ', '.join(result) + ']'
 words.sort()
 print 'Python的sort排序后: [' + ', '.join(words) + ']'
 print trie.find(trie.root,"北")
 print trie.findWords("北")
 os._exit(0)
