#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
#lexica.py
#
#autor: Rafael Alessandro Ramos
#date: 12-10-2017
#-------------------------------------------------------------------------

import ply.lex as lex

reserved = {
			'inteiro' 	: 'INTEIRO',
			'flutuante' : 'FLUTUANTE',
			'repita' 	: 'REPITA',
			'até' 		: 'ATE',
			'retorna' 	: 'RETORNA',
			'principal' : 'PRINCIPAL',
			'se' 		: 'SE',
			'então'		: 'ENTAO',
			'senão' 	: 'SENAO',
			'escreva' 	: 'ESCREVA',
			'leia' 		: 'LEIA',
			'fim' 		: 'FIM'
			}

tokens = [
		'SOMA',
		'SUBTRACAO',
		'MULTIPLICACAO',
		'DIVISAO', 
		'IGUALDADE', 
		'VIRGULA', 
		'ATRIBUICAO', 
		'MENOR', 
		'MAIOR', 
		'MENOR_IGUAL', 
		'MAIOR_IGUAL', 
		'ABRE_PAR', 
		'FECHA_PAR', 
		'DOIS_PONTOS', 
		'ABRE_COL',
		'FECHA_COL',
		'E_LOGICO', 
		'OU_LOGICO', 
		'ESPACO', 
		'NEGACAO',
		'ID',
		'NUMERO',
		'DECIMAL',
		'CIENTIFICA',
		'COMENTARIO'
		] + list(reserved.values())

# Regular expression rules for simple tokens
t_SOMA 			=	r'\+'
t_SUBTRACAO 	=	r'-'
t_MULTIPLICACAO =	r'\*'
t_DIVISAO 		=	r'/'
t_IGUALDADE 	=	r'='
t_VIRGULA 		=	r','
t_ATRIBUICAO 	=	r':='
t_MENOR 		=	r'\<'
t_MAIOR 		=	r'\>'
t_MENOR_IGUAL 	=	r'<='
t_MAIOR_IGUAL 	= 	r'>='
t_ABRE_PAR 		=	r'\('
t_FECHA_PAR 	=	r'\)'
t_DOIS_PONTOS 	= 	r':'
t_ABRE_COL 		=	r'\['
t_FECHA_COL 	=	r'\]'
t_E_LOGICO 		=	r'&&'
t_OU_LOGICO 	=	r'\|\|'
t_ESPACO 		=	r'\ '
t_NEGACAO 		=	r'\!'

def t_CIENTIFICA(t):
	r'((\d+)(\.\d+)(e(\+|\-)?(\d+)) | (\d+)e(\+|\-)?(\d+))'
	t.type = reserved.get(t.value,'CIENTIFICA')
	return t

def t_DECIMAL(t):
	r'\-?\d+\.+\d*'
	t.type = reserved.get(t.value,'DECIMAL')
	return t
	
def t_NUMERO(t):
	r'\-?\d+'
	t.type = reserved.get(t.value,'NUMERO')
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Zà-ú][a-zA-Zà-ú_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_COMENTARIO(t):
    r'\{[^}]*[^{]*\}'
    t.type = reserved.get(t.value,'COMENTARIO')
    return t


# Build the lexer
lexer = lex.lex()



# Abrir arquivo de teste
aux = False

# Test it out
try:
    string = open('multiplicavetor.tpp', 'r')  #Informe o arquivo que deseja varrer
    data = string.read()
    aux = True
except:
    print("ERRO AO ABRIR O ARQUIVO!!");

if aux:
	# Give the lexer some input
	lexer.input(data)

	# Tokenize
	while True:
		tok = lexer.token()
		if not tok: 
			break      # No more input
		print(tok)

