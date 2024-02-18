#!/usr/bin/env python
# coding: utf-8

# ---
# ## Sorbonne Université
# # <center> Mathématiques discrètes </center>
# ## <center> LU2IN005 </center>
# ## <div style="text-align:right;"> Année 2023-2024 </div>
# ---

# ---
# # <center> TME programmation d'automates finis </center>
# L'objectif de ce TME est de programmer en python quelques uns des
# algorithmes pour les automates finis vus en cours et en TD, en
# utilisant des structures de données fournies dans le code mis à votre
# disposition.
# ---
# # Consignes
# Copiez dans votre répertoire de travail les fichiers présents dans le Dossier 
# *Fichiers Python fournis* de la page Moodle de l'UE.
# 
# Ils contiennent les définitions de structures de données décrites
# ci-dessous, ainsi que des aide-mémoire sur l'utilisation de python.
# 
# **Le seul fichier que vous êtes autorisés à modifier** est celui-ci, c'est-à-dire
# `automate_etudiant.ipynb`, partiellement prérempli. 
# Les instructions `return` sont à supprimer lorsque
# vous remplirez le contenu des différentes fonctions.  Les autres
# fichiers n'ont pas besoin d'être lus (mais ils peuvent l'être).
# Si votre programme nécessite de lire des fichiers, **ceux-ci doivent être enregistrés dans le répertoire ExemplesAutomates** que vous avez téléchargé.
# ---


# ### Table des matières
# 
# > [1. Présentation](#sec1)
# >> [1.1 La classe `State`](#sec1_1) <br>
# >> [1.2 La classe `Transition`](#sec1_2) <br>
# >> [1.3 La classe `Automate`](#sec1_3)
# 
# > [2. Prise en mains](#sec2)
# >> [2.1 Création d'automates](#sec2_1) <br>
# >> [2.2 Premières manipulations](#sec2_2) <br>
# 
# > [3. Exercices de base : tests et complétion](#sec3)
# 
# > [4. Déterminisation](#sec4)
# 
# > [5. Constructions sur les automates réalisant des opérations sur les langages acceptés](#sec5)
# >> [5.1 Opérations ensemblistes sur les langages](#sec5_1) <br>
# >> [5.2 Opérations rationnelles sur les langages](#sec5_2)

# In[3]:


## Import des bibliothèques nécessaires au projet.
## Ne pas modifier les fichiers "bibliothèque".

## Interpréter cette cellule avant de continuer.

from transition import *
from state import *
import os
import copy
from automateBase import AutomateBase

class Automate(AutomateBase):
    pass


# ### 1. Présentation  <a class="anchor" id="sec1"></a>
# 
# Le projet utilise le langage python avec une syntaxe légèrement
# différente de celle vue en **LU1IN001 / 011**, parce qu'il exploite en particulier
# la notion de classes d'objets. Une introduction à cette notion est présentée dans le livre associé
# au cours : cf [Chapitre 13](https://www-licence.ufr-info-p6.jussieu.fr/lmd/licence/2021/ue/LU1IN001-2021oct/cours2020.pdf).
# 
# De plus, le typage des variables est noté de façon légèrement différente, en commentaires, pour les déclarations
# comme pour les arguments des fonctions. Pour ces derniers, les types sont indiqués dans la première ligne de la documentation de la fonction.
# 
# Les particularités sont brièvement expliquées en annexe
# de ce document. Par ailleurs, vous trouverez dans la section
# `projet` de la page Moodle un mémo sur la syntaxe python, ainsi que la carte de
# référence du langage utilisée en **LU1IN001 / 011**.  On rappelle qu'une ligne
# commençant par `#` est un commentaire, ignoré par
# l'interpréteur.
# 
# Toutes les structures de données nécessaires à la construction des
# automates sont fournies sous la forme de classes python, pour les
# transitions d'un automate, ses états, et les automates
# eux-mêmes. Cette section indique comment les utiliser.

# #### 1.1 La classe `State` <a class="anchor" id="sec1_1"></a>
# 
# Un état est représenté par
# - un entier `id` (type `int`) qui définit son identifiant,
# - un booléen `init` (type `bool`) indiquant si c'est un état initial,
# - un booléen `fin` (type `bool`) indiquant si c'est un état final,
# - une chaîne de caractères `label` (type `str`) qui définit son étiquette, permettant de le *décorer*. Par défaut, cette variable est la version chaîne de caractères de l'identifiant de l'état. 
# 
# On définit l'alias de type `State` pour représenter les variables de ce type. 
# 
# Ainsi, l'instruction ci-dessous crée une variable `s` représentant un état d'identifiant `1`, qui est un état initial mais pas final, dont l'identifiant et l'étiquette  `1` :

# In[4]:


# s : State
s = State(1, True, False)


# Si l'on souhaite avoir une étiquette différente de l'identifiant, on
# utilise un quatrième argument :

# In[5]:


s = State(1, True, False, 'etat 1') 


# On accède ensuite aux différents champs de `s` par la notation pointée : exécutez les cellules suivantes pour observer l'affichage obtenu.

# In[6]:


print('La valeur de s.id est : ')
print(s.id)


# In[7]:


print('La valeur de s.init est : ')
print(s.init)


# In[8]:


print('La valeur de s.fin est : ')
print(s.fin)


# In[9]:


print('La valeur de s.label est : ')
print(s.label)


# In[10]:


print("L'affichage de s est : ")
print(s)


# Ainsi, une variable de type `State` est affichée par son étiquette et, entre parenthèses, si c'est un état initial et/ou final.

# #### 1.2 La classe `Transition` <a class="anchor" id="sec1_2"></a>
# 
# Une transition est représentée par 
# - un état `stateSrc` (type `State`) correspondant à son état de départ
# - un caractère `etiquette` (type `str`) donnant son   étiquette
# - un état `stateDest` (type `State`) correspondant à son état de destination
# 
# On définit l'alias de type `Transition` pour représenter les variables de ce type.
# 
# La séquence d'instructions suivante crée la transition d'étiquette `"a"` de l'état `s` (défini ci-dessus) vers lui-même et affiche les différents champs de la transition :

# In[11]:


# t : Transition
t = Transition(s, "a", s)


# In[12]:


print('La valeur de t.etiquette est : ')
print(t.etiquette)


# In[13]:


print("L'affichage de t.stateSrc est : ")
print(t.stateSrc)


# On remarque que la variable `stateSrc` est de type `State`, on obtient donc un état, et non uniquement un
# identifiant d'état. 

# In[14]:


print("L'affichage de t.stateDest est : ")
print(t.stateDest)


# In[15]:


print("L'affichage de t est : ")
print(t)


# #### 1.3 La classe `Automate` <a class="anchor" id="sec1_3"></a>
# 
# Un automate est représenté par
# - l'ensemble de ses transitions `allTransitions` (de type `set[Transition]`) 
# - l'ensemble de ses états `allStates` (de type `set[State]`)
# - une étiquette `label` (de type `str`) qui est éventuellement vide.
# 
# On définit l'alias de type `Automate` pour représenter les variables de ce type.
# 
# Ainsi, de même que pour les classes précédentes, l'accès aux
# différents champs se fait par la notation pointée. Par exemple, on
# obtient l'ensemble des états d'un automate `monAutomate` par
# l'instruction `monAutomate.allStates`.
# 
# Pour créer un automate, il existe trois possibilités.

# **Création à partir d'un ensemble de transitions.**<br>
# On peut d'abord utiliser le constructeur de signature `Automate : set[Transition] -> Automate`.<br>
# Il déduit alors l'ensemble des états à partir de l'ensemble des transitions et définit par défaut l'étiquette
# de l'automate comme la chaîne de caractères vide.
# 
# Par exemple, en commençant par créer les états et les transitions nécessaires :

# In[16]:


## création d'états
# s1 : State
s1 = State(1, True, False)
# s2 : State
s2 = State(2, False, True)

## création de transitions
# t1 : Transition
t1 = Transition(s1,"a",s1)
# t2 : Transition
t2 = Transition(s1,"a",s2)
# t3 : Transition
t3 = Transition(s1,"b",s2)
# t4 : Transition
t4 = Transition(s2,"a",s2)
# t5 : Transition
t5 = Transition(s2,"b",s2)
# set_transitions : set[Transition]
set_transitions = {t1, t2, t3, t4, t5}

## création de l'automate
# aut : Automate
aut = Automate(set_transitions)


# L'affichage de cet automate, par la commande `print(aut)` produit alors le résultat suivant : 

# In[17]:


print(aut)


# Les états de l'automate sont déduits de l'ensemble de transitions.
# 
# Optionnellement, on peut donner un nom à l'automate, en utilisant la variable `label`, par exemple :

# In[18]:


# aut2 : Automate
aut2 = Automate(set_transitions, label="A") 

print(aut2)


# **Création à partir d'un ensemble de transitions et d'un ensemble d'états.**<br>
# Dans le second cas, on crée un automate à partir d'un ensemble de
# transitions mais aussi d'un ensemble d'états, par exemple pour représenter des
# automates contenant des états isolés. Pour cela, on utilise le
# constructeur `Automate : set[Transition] x set[State] -> Automate`.
# 
# On peut également, optionnellement, donner un nom à l'automate :

# In[19]:


# set_etats : set[State]
set_etats = {s1, s2}

# aut3 : Automate
aut3 = Automate(set_transitions, set_etats, "B")

print(aut3)


# L'ordre des paramètres peut ne pas être respecté **à la condition** que l'on donne leur nom explicitement. Ainsi, la ligne suivante est correcte :

# In[20]:


aut = Automate(setStates = set_etats, label = "A", setTransitions = set_transitions)

print(aut)


# **Création à partir d'un fichier contenant sa description.**<br>
# La fonction `Automate.creationAutomate : str -> Automate` prend en argument un nom de fichier qui décrit un automate et construit l'automate correspondant (voir exemple ci-dessous).
# 
# La description textuelle de l'automate doit suivre le format suivant (voir exemple ci-dessous) :
# - #E: suivi de la liste des noms des états, séparés par
#   des espaces ou des passages à la ligne. Les noms d'états peuvent
#   être n'importe quelle chaîne alphanumérique pouvant également
#   contenir le symbole `_`. Par contre, si le nom d'état
#   contient des symboles *non numériques* il ne doit pas commencer
#   par un chiffre, sous peine de provoquer une erreur à l'affichage.
#   Ainsi, `10` et `A1` sont des noms d'états possibles,
#   mais `1A` ne l'est pas.
# - #I: suivi de la liste des états initiaux
#   séparés par des espaces ou des passages à la ligne, 
# - #F: suivi de la liste des
#   états finaux séparés par des espaces ou des passages à la ligne, 
# - #T: suivi de la liste des transitions séparées par des
#   espaces ou des passages à la ligne. Chaque transition est donnée
#   sous le format `(etat1, lettre, etat2)`.
# 
# Par exemple le fichier `exempleAutomate.txt` contenant <br>
# `#E: 0 1 2 3`<br>
# `#I: 0`<br>
# `#F: 3`<br>
# `#T: (0 a 0)`<br>
# `	(0 b 0)`<br>
# `	(0 a 1)`<br>
# `	(1 a 2)`<br>
# `	(2 a 3)`<br>
# `	(3 a 3)`<br>
# `	(3 b 3)`<br>
# est formaté correctement. L'appel suivant produira l'affichage...

# In[21]:


# automate : Automate
automate = Automate.creationAutomate("ExemplesAutomates/exempleAutomate.txt")
print(automate)


# **Fonctions de manipulation des automates.**<br>
# La classe automate contient également de nombreuses fonctions utiles. Elles
# s'appliquent à un objet de type `Automate` et s'utilisent donc sous la forme
# `aut.<`*fonction*`>(<`*parametres*`>)` où `aut` est une variable de type `Automate`.
# 

# - `show : float -> NoneType` <br> 
#     prend en argument facultatif un flottant (facteur de grossissement, par défaut il vaut 1.0) et produit une représentation graphique de l'automate.<br>
#     Ainsi, en utilisant l'automate défini dans le fichier d'exemple précédent, l'instruction `automate.show(1.2)` produit l'image suivante :

# In[22]:


automate.show(1.2,'affichage.dot')


# - `addTransition : Transition -> bool`<br>
#   prend en argument une transition `t`, fait la mise à jour de
#   l'automate en lui ajoutant `t` et ajoute les états impliqués
#   dans l'automate s'ils en sont absents. Elle rend `True` si l'ajout a
#   eu lieu, `False` sinon (si `t` était déjà présente dans l'automate).
#   
# - `removeTransition : Transition -> bool`<br>
#   prend en argument une transition `t` et fait la mise à jour de
#   l'automate en lui enlevant la transition, sans modifier les
#   états. Elle rend `True` si la suppression a eu lieu, `False` sinon (si
#   `t` était absente de l'automate).
# 
# - `addState : State -> bool`<br>
#   prend en argument un état `s` et fait la mise à jour de
#   l'automate en lui ajoutant `s`.  Elle rend `True` si l'ajout a eu
#   lieu, `False` sinon (si `s` était déjà présent dans l'automate).
# 
# - `nextId : -> int`<br>
#   renvoie un entier id frais, en choisissant l'entier le plus petit,
#   strictement supérieur à tous les id des états de l'automate.
# 
# - `removeState : State -> bool`<br>
#   prend en argument un état `s` et fait la mise à jour de
#   l'automate en supprimant `s` ainsi que toutes ses transitions
#   entrantes et sortantes.  Elle rend `True` si l'ajout a eu lieu, `False`
#   sinon (si `s` était absent de l'automate).
#   
# - `getSetInitialStates :  -> set[State]`<br> 
#   rend l'ensemble des états initiaux.
# 
# - `getSetFinalStates :  -> set[State]`<br>
#   rend l'ensemble des états finaux.
# 
# - `getSetTransitionsFrom : State -> set[Transition]`<br>
#   rend l'ensemble des transitions sortant de l'état passé en argument.
# 
# - `prefixStates : int -> NoneType`<br>
#   modifie les identifiants et les étiquettes de tous les états de
#   l'automate en les préfixant par l'entier passé en argument.
# 
# - `succElem : State x str -> set[State]`<br>
#   étant donné un état `s` et un caractère `a`, elle rend l'ensemble des
#   états successeurs de `s` par le caractère `a`.  Formellement,
#   
#   $$succElem(s, a) = \{s' \in S \mid  s \xrightarrow{a} s'\}.$$
#   
#   Cet ensemble peut contenir plusieurs états si l'automate n'est pas déterministe.

# In[23]:


# Voilà le code de succElem

def succElem(self, state, lettre):
    """ State x str -> set[State]
        rend l'ensemble des états accessibles à partir d'un état state par l'étiquette lettre
    """
    successeurs = set()
    # t: Transitions
    for t in self.getSetTransitionsFrom(state):
        if t.etiquette == lettre:
            successeurs.add(t.stateDest)
    return successeurs

Automate.succElem = succElem


# Avec l'exemple précédent, on obtient :

# In[24]:


s0 = list(automate.getSetInitialStates())[0] ## on récupère l'état initial de automate
automate.succElem(s0, 'a')


# ### 2. Prise en mains  <a class="anchor" id="sec2"></a>
# 
# #### 2.1 Création d'automates <a class="anchor" id="sec2_1"></a>
# 
# Soit l'automate $\mathcal{A}$ défini sur l'alphabet $\{ a,b \}$, d'états $0,1,2$, 
# d'état initial 0, d'état final 2 et de transitions : <br>$(0,a,0)$, $(0,b,1)$, 
# $(1,a,2)$, $(1,b,2)$, $(2,a,0)$ et $(2,b,1)$.
# 
# 1. Créer l'automate $\mathcal{A}$ à l'aide de son ensemble de transitions. Pour cela, créer un état `s0`  
# d'identifiant $0$
#   qui soit initial, un état `s1` d'identifiant $1$ et un état
#   `s2` d'identifiant $2$ qui soit final. Puis créer `t1`, `t2`, `t3`, `t4`, `t5` et
#   `t6` les 6 transitions de l'automate. Créer enfin l'automate
#   `auto` à partir de ses transitions, par exemple avec l'appel<br>
#   `auto = Automate({t1,t2,t3,t4,t5,t6})`.<br>
#   Vérifier que l'automate correspond bien à $\mathcal{A}$ en l'affichant.

# In[25]:


# A faire 
## création d'états
# s0 : State
s0 = State(0, True, False)
# s1 : State
s1 = State(1, False, False)
s2 = State(2, False , True)

## création de transitions
# t1 : Transition
t1 = Transition(s0,"a",s0)
# t2 : Transition
t2 = Transition(s0,"b",s1)
# t3 : Transition
t3 = Transition(s1,"a",s2)
# t4 : Transition
t4 = Transition(s1,"b",s2)
# t5 : Transition
t5 = Transition(s2,"a",s0)
# t6 : Transition
t6 = Transition(s2,"b",s1)
# set_transitions : set[Transition]
set_trans = {t1, t2, t3, t4, t5, t6}

## création de l'automate
# aut : Automate
auto = Automate(set_trans)
print(auto)
auto.show(1.2)


# 2. Créer l'automate $\mathcal{A}$ à l'aide de sa liste de
#   transitions et d'états, par exemple à l'aide de l'appel<br>
#   `auto1 = Automate({t1,t2,t3,t4,t5,t6}, {s0,s1,s2})`<br>
#   puis afficher l'automate obtenu à l'aide de `print` puis à l'aide de `show`.
#   Vérifier que l'automate `auto1` est bien
#   identique à l'automate `auto`.

# In[26]:


# A faire 
## création d'états
# s0 : State
s0 = State(0, True, False)
# s1 : State
s1 = State(1, False, False)
# s2 : State
s2 = State(2, False , True)

## création de transitions
# t1 : Transition
t1 = Transition(s0,"a",s0)
# t2 : Transition
t2 = Transition(s0,"b",s1)
# t3 : Transition
t3 = Transition(s1,"a",s2)
# t4 : Transition
t4 = Transition(s1,"b",s2)
# t5 : Transition
t5 = Transition(s2,"a",s0)
# t6 : Transition
t6 = Transition(s2,"b",s1)
# set_transitions : set[Transition]
set_trans = {t1, t2, t3, t4, t5, t6}
set_etats = {s0, s1, s2}
## création de l'automate
# aut : Automate
auto1 = Automate(set_trans,set_etats)
print(auto1)
auto1.show(1.2)
print("Les 2 automates sont identiques : {} ".format(auto1.equals(auto)))


# 3. Créer l'automate $\mathcal{A}$ à partir d'un fichier. Pour cela,
#   créer un fichier `auto2.txt`, dans lequel sont indiqués les
#   listes des états et des transitions, ainsi que l'état initial et
#   l'état final, en respectant la syntaxe donnée dans la section
#   précédente. Par exemple la liste d'états est décrite par la ligne
#   `#E: 0 1 2`.  Utiliser ensuite par exemple l'appel
#   `auto2 = Automate.creationAutomate("ExemplesAutomates/auto2.txt")`, puis afficher
#   l'automate `auto2` à l'aide de `print` ainsi qu'à l'aide de `show`.

# In[27]:


# A faire
auto2 = Automate.creationAutomate("ExemplesAutomates/auto2.txt")
print(auto2)
auto2.show(1.2)
print("Les 2 automates sont identiques : {} ".format(auto1.equals(auto2)))


# #### 2.2 Premières manipulations <a class="anchor" id="sec2_2"></a>
# 
# 1. Appeler la fonction `removeTransition` sur l'automate
#   `auto` en lui donnant en argument la transition $(0,a,1)$. Il
#   s'agit donc de créer une variable `t` de type
#   `Transition` représentant $(0,a,1)$ et d'effectuer l'appel
#   `auto.removeTransition(t)`. Observer le résultat sur un
#   affichage.  Appeler ensuite cette fonction sur `auto` en lui
#   donnant en argument la transition `t1`. Observer le résultat
#   sur un affichage. Appeler la fonction `addTransition` sur
#   l'automate `auto` en lui donnant en argument la transition
#   `t1`. Vérifier que l'automate obtenu est bien le même
#   qu'initialement.

# In[28]:


# A faire
t = Transition(s0,"a",s1)
auto.removeTransition(t)
print("Transition t existe dans automate auto : {}".format(auto.removeTransition(t)))
auto.show()
auto.removeTransition(t1)
print("remove transition (0,a,a)")
auto.show()
print("rajout transition (0,a,a)")
auto.addTransition(t1)
auto.show()
print("Les 2 automates sont identiques : {} ".format(auto.equals(auto1)))


# 2. Appeler la fonction `removeState` sur l'automate
#   `auto` en lui donnant en argument l'état
#   `s1`. Observer le résultat. Appeler la fonction
#   `addState` sur l'automate `auto` en lui donnant en
#   argument l'état `s1`. Créer un état `s0bis` d'identifiant
#   $0$ et initial. Appeler la fonction `addState` sur
#   `auto` avec `s0bis` comme argument. Observer le résultat.

# In[29]:


# A faire 
print(auto)
auto.removeState(s1)
print(auto)
auto.show(0.5)

auto.addState(s1)
print(auto)
s0bis = State(0,True,False)
auto.addState(s0bis)
print(auto)
auto.show(0.5)



# 3. Appeler la fonction `getSetTransitionsFrom` sur
#   l'automate `auto1` avec `s1` comme argument. Afficher
#   le résultat.

# In[30]:


# A faire
auto1.getSetTransitionsFrom(s1)
#transitions sortant de l'état s1 dans auto1


# ### 3. Exercices de base : tests et complétion  <a class="anchor" id="sec3"></a>

# 1. Donner une définition de la fonction `succ`
#   qui, étant donné un ensemble d'états $S$ et une chaîne de caractères
#       $a$ (de longueur 1), renvoie l'ensemble des états successeurs de tous les états de $L$ par le caractère $a$. Cette fonction doit généraliser la fonction `succElem` pour qu'elle prenne en paramètre un ensemble d'états au lieu d'un seul état.  Formellement, si $S$ est un ensemble d'états et $a$ une lettre,
#   $$succ(S,a) = \bigcup_{s \in S}succ(s,a) = \{s' \in S \mid \mbox{il
#     existe } s \in L \mbox{ tel que } s \xrightarrow{a} s'\}.$$

# In[31]:


# A faire 

def succ(self, setStates, lettre):
    """ Automate x set[State] x str -> set[State]
        rend l'ensemble des états accessibles à partir de l'ensemble d'états setStates par l'étiquette lettre
    """
    ensembleSuccesseur = set()
    for state in setStates : 
        ensembleSuccesseur = ensembleSuccesseur.union(self.succElem(state,lettre))
    return ensembleSuccesseur

Automate.succ = succ



# In[32]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.succ({s0, s2}, 'b') == {s1}
assert auto1.succ({s0}, 'a') == {s0}
assert auto1.succ({s0, s1}, 'a') == {s0, s2}


# In[33]:


# Fournir un autre jeu de tests
assert auto1.succ({s1, s2, s0}, 'a') == {s2, s0, s0}
assert auto1.succ({s1}, 'b') == {s2}
assert auto1.succ({s2, s0}, 'a') == {s0}
print("les tests se sont bien passés")


# 2. Donner une définition de la fonction `accepte`
#   qui, étant donné une chaîne de caractères `mot`,
#   renvoie un booléen qui vaut vrai si et seulement si `mot` est accepté par l'automate. Attention, noter que l'automate peut ne pas être déterministe.

# In[34]:


# A faire 
#derniere lettre arrive a un etat final
def accepte(self, mot) :
    """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
    """
    states = self.getSetInitialStates()
    for a in mot :
        states = self.succ(states, a)
    for st in states:
        if st.fin:
            return True
    return False

Automate.accepte = accepte


# In[35]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.accepte('aa') == False
assert auto1.accepte('aba') == True
assert auto1.accepte('ab') == False




# In[36]:


# Fournir un autre jeu de tests
print('---')
assert auto1.accepte('abbaba') == True
assert auto1.accepte('babb') == True
assert auto1.accepte('ababb') == True

assert auto1.accepte('abaa') == False
assert auto1.accepte('babaa') == False
assert auto1.accepte('bbb') == False


# 3. Donner une définition de la fonction `estComplet`
#     qui, étant donné un automate `auto` et un ensemble de caractères `Alphabet`
#     renvoie un booléen qui vaut vrai si et
#     seulement si `auto` est complet par rapport à l'alphabet.
#     
#     On n'effectuera pas la vérification sur les états non accessibles depuis les états initiaux.

# In[37]:


# A faire 

def estComplet(self, Alphabet) :
    """ Automate x set[str] -> bool
        rend True si auto est complet pour les lettres de Alphabet, False sinon
        hyp : les éléments de Alphabet sont de longueur 1
    """
#chaque état au moins une transition sortante pour chaque lettre 
    for s in self.allStates :
        for a in Alphabet :
            if not self.succElem(s, a):
                return False 
    return True


Automate.estComplet = estComplet



# In[38]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.estComplet({'a', 'b'}) == True
assert auto1.estComplet({'a', 'c', 'b'}) == False


# In[39]:


# Fournir un autre jeu de tests
automate.show()
print('---')
assert automate.estComplet({'a', 'b'}) == False
assert automate.estComplet({'a'}) == True
assert automate.estComplet({'b'}) == False



# 4. Donner une définition de la fonction `estDeterministe`
# qui, étant donné un automate `auto`,
#  renvoie un booléen qui vaut vrai si et seulement si `auto` est déterministe.

# In[40]:


# A faire 

def estDeterministe(self) :
    """ Automate -> bool
        rend True si auto est déterministe, False sinon
    """
    #1 unique etat initial
    if len(self.getSetInitialStates())!=1:  
            return False
    else: 
        for s in self.allStates:
            for a in self.getAlphabetFromTransitions():
                transitions = self.succElem(s, a)
                if len(transitions) > 1: #1 transition sortante pour chaque etat et chaque lettre
                    return False

    return True 
    
Automate.estDeterministe = estDeterministe


# L'appel de fonction `copy.deepcopy(auto)` renvoie un nouvel automate identique à `auto`.

# In[41]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.estDeterministe() == True

auto1bis = copy.deepcopy(auto1)
#t : Transition
t = Transition(s1, 'b', s0)
auto1bis.addTransition(t)
auto1bis.show()
print('---')
assert auto1bis.estDeterministe() == False

auto1bis.removeTransition(t)
auto1bis.show()
print('---')
assert auto1bis.estDeterministe() == True


# In[42]:


# Fournir un autre jeu de tests

automate.show()
print('---')
assert automate.estDeterministe() == False


# 5. Donner une définition de la fonction `completeAutomate`
# qui, étant donné un automate `auto` et l'ensemble alphabet d'entrée `Alphabet`,
# renvoie l'automate complété d'`auto`.
#   
# Attention, il ne faut pas modifier `auto`, mais construire un nouvel automate.
# <br>Il pourra être intéressant d'utiliser l'appel de fonction
# `copy.deepcopy(auto)` qui renvoie un nouvel automate identique à `auto`.
# <br>On pourra faire appel à la fonction `nextId` afin de construire l'état $\bot$.

# In[43]:


# A faire
#Ajouter un état puits P ; 
#Ajouter pour chaque état q, et chaque lettre α, une transition (q, α, P) s’il n’existe pas déjà 
#une transition partant de q par la lettre α. 
#Pour chaque lettre α, ajouter la transition (P, α, P).

def completeAutomate(self, Alphabet) :
    """ Automate x str -> Automate
        rend l'automate complété de self, par rapport à Alphabet
    """ 
    autocopy = copy.deepcopy(self)
    if self.estComplet(Alphabet):
        return autocopy 
    else : 
        etatpuit = State(autocopy.nextId(),False,False,"P")
        autocopy.addState(etatpuit)
        for a in Alphabet : 
            autocopy.addTransition(Transition(etatpuit,a,etatpuit))
            for s in autocopy.allStates : 
                if not self.succElem(s,a) :
                    autocopy.addTransition(Transition(s,a,etatpuit))
        return autocopy

Automate.completeAutomate = completeAutomate


# In[44]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant :

auto1.show()
print('---')
assert auto1.estComplet({'a', 'b'}) == True
auto1complet = auto1.completeAutomate({'a', 'b'})
auto1complet.show()
assert auto1complet.estComplet({'a', 'b'}) == True

print('---')
assert auto1.estComplet({'a', 'b', 'c'}) == False
auto1complet = auto1.completeAutomate({'a', 'b', 'c'})
auto1complet.show()
assert auto1complet.estComplet({'a', 'b','c'}) == True


# In[45]:


# Fournir un autre jeu de tests
automate.show()
print('---')
assert automate.estComplet({'a', 'b'}) == False
automatecomplet = automate.completeAutomate({'a', 'b'})
automatecomplet.show()
assert automatecomplet.estComplet({'a', 'b'}) == True


# ### 4. Déterminisation  <a class="anchor" id="sec4"></a>

# 1. Donner une définition de la fonction `newLabel`
# qui, étant donné un ensemble d'états renvoie une *chaîne de caractères* représentant l'ensemble de tous les labels des états.
# Par exemple, l'appel de `newLabel` sur un ensemble de 3 états dont les labels sont `'1', '2', '3'` renvoie `'{1,2,3}'`
# 
# Afin d'être assuré que l'ordre de parcours de l'ensemble des états n'a pas d'importance, il sera nécessaire de trier par ordre alphabétique la liste des `label` des états. On pourra faire appel à `L.sort()` qui étant donné la liste `L` de chaînes de caractères, la trie en ordre alphabétique.

# In[46]:


# A faire

def newLabel(S):
    """ set[State] -> str """
    labels = list(S)
    chaine = "{"
    if labels:
        for i in range(0, len(labels) - 1):
            chaine = chaine + str(labels[i].id) + ','
        chaine = chaine + str(labels[len(labels) - 1].id)
    chaine += "}"
    return chaine


# In[47]:


# On a défini auparavant un automate auto1, voilà un test le concernant :
assert newLabel(auto1.allStates) == '{0,1,2}'


# In[48]:


# Fournir un autre jeu de tests
assert newLabel(automate.allStates) == '{0,1,2,3}'
labels = {s2,s1,s1}
assert newLabel(labels) == '{1,2}'
print(newLabel(automate.getSetInitialStates()))
print(newLabel({s0,s1}))


# La fonction suivante permet de déterminiser un automate. On remarque qu'un état peut servir de clé dans un dictionnaire.

# In[49]:


def determinisation(self) :
    """ Automate -> Automate
    rend l'automate déterminisé de self """
    if self.estDeterministe() : 
        return self
    # Ini : set[State]
    Ini = self.getSetInitialStates()
    # fin : bool
    fin = False
    # e : State
    for e in Ini:
        if e.fin:
            fin = True
    lab = newLabel(Ini)
    s = State(0, True, fin, lab)
    A = Automate(set())
    A.addState(s)
    Alphabet = {t.etiquette for t in self.allTransitions}
    Etats = dict()
    Etats[s] = Ini
    A.determinisation_etats(self, Alphabet, [s], 0, Etats, {lab}) #[s] etat initial et de depart {0}
    return A


# L'automate déterminisé est construit dans `A`. Pour cela la fonction récursive `determinisation_etats` modifie en place l'automate `A`, et prend en outre les paramètres suivants :
# - `auto`, qui est l'automate de départ à déterminiser
# - `Alphabet` qui contient l'ensemble des lettres étiquetant les transistions de l'automate de départ
# - `ListeEtatsATraiter` qui est la liste des états à ajouter et à traiter dans `A` au fur et à mesure que l'on progresse dans `auto`.
# - `i` qui est l'indice de l'état en cours de traitement (dans la liste `ListeEtatsATraiter`).
# - `Etats` qui est un dictionnaire dont les clés sont les états de `A` et les valeurs associées sont l'ensemble d'états issus de `auto` que cette clé représente.
# - `DejaVus` est l'ensemble des labels d'états de `A` déjà vus.

# In[50]:


# A faire 
"""Etats : Un dictionnaire associant chaque état de l'automate déterminisé à l'ensemble d'états de l'automate initial qu'il représente."""
def determinisation_etats(self , auto , Alphabet, ListeEtatsATraiter, i, Etats, DejaVus):
    """ Automate x Automate x set[str] x list[State] x int x dict[State : set[State]], set[str] -> NoneType
    """
    #vérifie si on a traité tous les états dans ListeEtatsATraiter. 
    if i >= len(ListeEtatsATraiter) :
        return
    
    etatEnTraitement = ListeEtatsATraiter[i]
    DejaVus.add(etatEnTraitement.label)
    
    setEtatsFromTraitement = Etats[etatEnTraitement]
    setEtatsFin = auto.getSetFinalStates()
    
    for lettre in Alphabet :
        EtatsSucc = auto.succ(setEtatsFromTraitement, lettre)
        label = newLabel(EtatsSucc)
        
        # Si le label est nouveau et des états successeurs existent (pour ne pas creer etat {}), on crée un nouvel état.
        if label not in DejaVus and EtatsSucc:
            testFinal = setEtatsFin.intersection(EtatsSucc) != set()
            
            newEtat = State(self.nextId(), False, testFinal, label)
            Etats[newEtat] = EtatsSucc # On rajoute les états successeurs dans le dictionnaire Etats.
            
            newTrans = Transition(etatEnTraitement, lettre, newEtat)# On crée et ajoute la nouvelle transition.
            self.addTransition(newTrans)
            
            # On rajoute le nouvel état dans la liste à traiter et on rajoute le label de l'état en traitement dans DejaVus.
            ListeEtatsATraiter.append(newEtat)
            DejaVus.add(label)
            
        
        # Sinon, on rajoute la transition, sans créer de nouvel état, uniquement si des états successeurs existent.
        elif EtatsSucc:
            for oldEtat in ListeEtatsATraiter:
                if oldEtat.label == label:
                    newT = Transition(etatEnTraitement, lettre, oldEtat)
                    self.addTransition(newT)
                    break
    
    #recursive etat suivant
    self.determinisation_etats(auto, Alphabet, ListeEtatsATraiter, i+1, Etats, DejaVus)


Automate.determinisation_etats = determinisation_etats
Automate.determinisation = determinisation


# In[51]:


# Voici un test
#automate est l'automate construit plus haut a partir du fichier exempleAutomate.txt
automate = Automate.creationAutomate("ExemplesAutomates/exempleAutomate.txt")
automate.show()
auto_det = automate.determinisation()
print(auto_det.estDeterministe())
auto_det.show(2)


# In[52]:


#Fournir d'autres jeux de tests
automateAdeterminiser = Automate.creationAutomate("ExemplesAutomates/auto3.txt")
automateAdeterminiser.show()
auto_deter = automateAdeterminiser.determinisation()
print(auto_deter.estDeterministe())
auto_deter.show(2)

auto_deter1=auto1.determinisation()
auto_deter1.show()


# ### 5. Constructions sur les automates réalisant  des opérations sur les langages acceptés <a class="anchor" id="sec5"></a>
# 
# 
# #### 5.1 Opérations ensemblistes sur les langages <a class="anchor" id="sec5_1"></a>
# 
# 1. Donner une définition de la fonction `complementaire` qui, étant donné un automate `auto` et un ensemble de caractères `Alphabet`, renvoie l'automate acceptant la langage complémentaire du langage accepté par `auto`. Ne pas modifier l'automate `auto`, mais construire un nouvel automate.

# In[53]:


#A faire
#etats finaux deviennet non finaux et vice versa
def complementaire(self, Alphabet):
    """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de self
    """
    deterETcomplet = self.completeAutomate(Alphabet).determinisation()
    for x in deterETcomplet.allStates:
        x.fin = not x.fin
    return deterETcomplet
    
Automate.complementaire = complementaire   


# In[54]:


# Voici un test

automate = Automate.creationAutomate("ExemplesAutomates/exempleAutomate.txt")
automate.show()
Alphabet = {t.etiquette for t in auto.allTransitions}
auto_compl = automate.complementaire(Alphabet)
auto_compl.show(2)


# In[55]:


#Fournir d'autres tests
auto1.show()
Alphabet = {t.etiquette for t in auto1.allTransitions}
auto_complet = auto1.complementaire(Alphabet)
auto_complet.show()


# 2. Donner une définition de la fonction `intersection` qui, étant donné deux automates `auto1` et `auto2`, renvoie l'automate acceptant l'intersection des langages acceptés par `auto1` et `auto2`.
# 
# L'automate construit ne doit pas avoir d'état non accessible depuis l'état initial.

# In[56]:


#A faire

def intersection(self, auto):
    """ Automate x Automate -> Automate
    rend l'automate acceptant pour langage l'intersection des langages des deux automates
    """
    #ensembles d'états finaux et initiaux pour chaque automate
    finaux1 = self.getSetFinalStates()
    finaux2 = auto.getSetFinalStates()
    initiaux1 = self.getSetInitialStates()
    initiaux2 = auto.getSetInitialStates()
    
    #les paires d'états = nouveaux états
    setTransitions = set()
    dic = dict()
    l = []
    
    i = 0
    #nouveaux états pour chaque paire d'états initiaux des deux automates
    for etat1 in initiaux1:
        for etat2 in initiaux2:
            # la paire d'états clé de dic
            dic[(etat1, etat2)] = State(i, True, etat1 in finaux1 and etat2 in finaux2, '('+etat1.label+','+etat2.label+')')
            l.append((etat1, etat2)) 
            i += 1
                
    #Pour chaque paire d'états,nouvelles transitions basées sur les transitions correspondantes des automates d'origine
    for etat1, etat2 in l:
        for t1 in self.getSetTransitionsFrom(etat1): #transitions sortant de etat1
            for t2 in auto.getSetTransitionsFrom(etat2):
                # Si meme etiquettes de transitions
                if t1.etiquette == t2.etiquette:
                    #Si la paire d'états destination n'a pas encore été créée, on cree un nouvel état et ajout au dictionnaire
                    if (t1.stateDest, t2.stateDest) not in dic:
                        dic[(t1.stateDest, t2.stateDest)] = State(i, t1.stateDest in initiaux1 and t2.stateDest in initiaux2, t1.stateDest in finaux1 and t2.stateDest in finaux2, '('+t1.stateDest.label+','+t2.stateDest.label+')')
                        l.append((t1.stateDest, t2.stateDest))
                        i += 1
                    # ajout des nouvelles transitions avec les nouveaux etats
                    setTransitions.add(Transition(dic[(t1.stateSrc, t2.stateSrc)], t1.etiquette, dic[t1.stateDest, t2.stateDest]))
  
    #nvl trans
    autoRes = Automate(setTransitions)
    return autoRes
    
    
Automate.intersection = intersection


# In[57]:


#Un premier test

automate.show()
auto2.show()
inter = automate.intersection(auto2)
inter.show(2)


# In[58]:


# Fournir d'autres tests
automate3 = Automate.creationAutomate("ExemplesAutomates/auto3.txt")
automate3.show()
auto2.show()
intersec = automate3.intersection(auto2)
intersec.show()


# 3. (Question facultative) Donner une définition de la fonction `union` qui, étant donné deux automates `auto1` `auto2`, renvoie l'automate acceptant comme langage l'union des langages acceptés par `auto1` et `auto2`.

# In[59]:


#A faire par l'étudiant

def union(self, auto):
    """ Automate x Automate -> Automate
    Rend l'automate acceptant l'union des langages des deux automates
    """
    #on complete l'automate si pas complet
    if not self.estComplet(self.getAlphabetFromTransitions()):
        self = self.completeAutomate(self.getAlphabetFromTransitions())
    elif not auto.estComplet(auto.getAlphabetFromTransitions()):
        auto = auto.completeAutomate(auto.getAlphabetFromTransitions())
    
    #Ensembles d'états finaux et initiaux pour chaque automate
    finaux1 = self.getSetFinalStates()
    finaux2 = auto.getSetFinalStates()
    initiaux1 = self.getSetInitialStates()
    initiaux2 = auto.getSetInitialStates()

    #Ensembles de transitions pour le nouvel automate
    setTransitions = set()

    #Dictionnaire pour mapper les paires d'états à de nouveaux états
    dic = dict()
    l = []

    i = 0
    #nouveaux états pour chaque paire d'états initiaux des deux automates
    for etat1 in initiaux1:
        for etat2 in initiaux2:
            # La paire d'états clé de dic
            dic[(etat1, etat2)] = State(i, etat1.init or etat2.init, etat1.fin or etat2.fin, '('+etat1.label+','+etat2.label+')')
            l.append((etat1, etat2))
            i += 1

    #Pour chaque paire d'états,nouvelles transitions basées sur les transitions correspondantes des automates d'origine
    for etat1, etat2 in l:
        for t1 in self.getSetTransitionsFrom(etat1): #transitions sortant de etat1
            for t2 in auto.getSetTransitionsFrom(etat2):
                # Si meme etiquettes de transitions
                if t1.etiquette == t2.etiquette:
                    # Si la paire d'états destination n'a pas encore été créée,on cree un nouvel état et ajout au dictionnaire
                    if (t1.stateDest, t2.stateDest) not in dic:
                        dic[(t1.stateDest, t2.stateDest)] = State(i, t1.stateDest in initiaux1 and t2.stateDest in initiaux2, t1.stateDest in finaux1 or t2.stateDest in finaux2, '('+t1.stateDest.label+','+t2.stateDest.label+')')
                        l.append((t1.stateDest, t2.stateDest))
                        i += 1
                    #ajout des nouvelles transitions avec les nouveaux etats
                    setTransitions.add(Transition(dic[(t1.stateSrc, t2.stateSrc)], t1.etiquette, dic[t1.stateDest, t2.stateDest]))
  
    #nvl trans
    autoRes = Automate(setTransitions)
    return autoRes

Automate.union = union


# In[60]:


#Un premier test

automate.show()
auto2.show()
uni = automate.union(auto2)
uni.show(2)


# In[61]:


automate3 = Automate.creationAutomate("ExemplesAutomates/auto3.txt")
automate3.show()
auto2.show()
uni = automate3.union(auto2)
uni.show()


# #### 5.2 Opérations rationnelles sur les langages <a class="anchor" id="sec5_2"></a>
# 
# Programmer *une des deux* méthodes suivantes:
# 
# 1. Donner une définition de la fonction `concatenation` qui, étant donné deux automates `auto1` et `auto2`, renvoie l'automate acceptant comme langage la concaténation des langages acceptés par `auto1` et `auto2`.
# 
# 2. Donner une définition de la fonction `etoile` qui, étant donné un automate `auto`, renvoie l'automate acceptant comme langage l'étoile du langages accepté par `auto`.

# In[62]:


# A faire
def concatenation(self, auto):
    """ Automate x Automate -> Automate
    rend l'automate acceptant pour langage la concaténation des langages des deux automates
    """
    Alphabets = self.getAlphabetFromTransitions()

    #copie les automates
    selfcopy = copy.deepcopy(self)
    autocopy = copy.deepcopy(auto)

    #etat initiaux de auto et finaux de self
    initiauxAuto = autocopy.getSetInitialStates()
    finauxSelf = selfcopy.getSetFinalStates()

    #états finaux de self deviennet non finaux
    for etat in finauxSelf:
        etat.fin = False

    #états initiaux de auto deviennet non initiaux si le mot vide n'est pas accepté
    for etat in initiauxAuto:
        etat.init = False

    #setransitions pour le nouvel automate pour linstant que du self
    setTransitions = selfcopy.allTransitions
    
    DejaVus = set()#suivre id state traités
    i = self.nextId()#prochain id 

    #máj des id de tous les states de auto et rajout des transitions de auto dans setTransitions
    for t in autocopy.allTransitions:
        if t.stateSrc.id not in DejaVus:
            t.stateSrc.id = i #change id
            t.stateSrc.label = i #change label
            i += 1
            DejaVus.add(t.stateSrc.id)
        if t.stateDest.id not in DejaVus:
            t.stateDest.id = i
            t.stateDest.label = i
            i += 1
            DejaVus.add(t.stateDest.id)
        setTransitions.add(t)

        
    #ajout transitions de concatenation

    for etat in self.allStates:
        for etatfin in finauxSelf:
            for l in Alphabets:
                #si etat final est successeur d'un etat de self par l on rajoute transition 
                if etatfin in self.succElem(etat, l): 
                    for etatini in initiauxAuto:
                        t = Transition(etat, l, etatini)
                        setTransitions.add(t)

    #nvl automate 
    autores = Automate(setTransitions)

    return autores

Automate.concatenation = concatenation


# In[63]:


#Un premier test
automate.show()
auto2.show()
concat = automate.concatenation(auto2)
concat.show(2)


# In[64]:


#Fournir un autre jeu de test
automate3.show()
auto2.show()
concat2=automate3.concatenation(auto2)
concat2.show(2)


# In[65]:


def etoile (self):
    """ Automate  -> Automate
    rend l'automate acceptant pour langage l'étoile du langage de a
    """
    auto = copy.deepcopy(self)
    
    #état initial en meme temps final pour accepter mot vide
    etatepsilon = State(auto.nextId(), True, True, "e")
    
    setEtatsInit = auto.getSetInitialStates()
    setEtatsFin = auto.getSetFinalStates()
    
    #creation des transitions etat epsilon et les successeurs des états init
    for etatInit in setEtatsInit :
        for t in auto.getSetTransitionsFrom(etatInit) :
            newTrans = Transition(etatepsilon, t.etiquette, t.stateDest)
            auto.addTransition(newTrans)

    # transitions pour que tout mots acceptés 
    # de l'état final a dest de etat epsilon       
    for t in auto.getSetTransitionsFrom(etatepsilon) :
        for etatFin in setEtatsFin :
            newTrans = Transition(etatFin, t.etiquette, t.stateDest)
            auto.addTransition(newTrans)
            
    #seul etat epsilon est initial et final
    for etat in auto.allStates :
        etat.init = False
        etat.fin = False
    etatepsilon.init = True
    etatepsilon.fin = True
        
    return auto


Automate.etoile = etoile


# In[69]:


#liaison epsilon de etat final a etat initial 
#eliminer liaison epsilon 
def etoile2 (self):
    """ Automate  -> Automate
    rend l'automate acceptant pour langage l'étoile du langage de a
    """
    auto = copy.deepcopy(self)
    Alphabets = auto.getAlphabetFromTransitions()
    setEtatsInit = auto.getSetInitialStates()
    setEtatsFin = auto.getSetFinalStates()
    
    # Ajout des transitions pour que tous les mots soient acceptés
    for etat in auto.allStates:
        for etatFin in setEtatsFin:
            for l in Alphabets:
                # Si etatFin est successeur d'un état de auto par l, ajout la transition
                if etatFin in auto.succElem(etat, l):
                    for etatInit in setEtatsInit:
                        auto.addTransition(Transition(etat, l, etatInit))
            
        
    return auto

Automate.etoile2 = etoile2


# In[70]:


#Un premier test

automate.show()
autoetoile = automate.etoile2()
autoetoile.show()


# In[71]:


#Fournir un autre jeu de tests
auto2.show()
autoetoile2 = auto2.etoile2()
autoetoile2.show()


# In[73]:


#Fournir un autre jeu de tests
#exemple de diapo de cour
automate4 = Automate.creationAutomate("ExemplesAutomates/auto4.txt")
automate4.show()
autoetoile4 = automate4.etoile2()
autoetoile4.show()

