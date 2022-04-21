
#note: covenants accrue about 25bp per year of existence based on Covenants pg. 5

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, OptionMenu, ttk
import random
import csv

class Book:
	def __init__(self,type,title,subject,quality,level,desc,value):
		self.type = type
		self.title = title
		self.subject = subject
		self.quality = quality
		self.level = level
		self.desc = desc
		self.value = value
		
	def getDescription(self):
		ret_string = ""
		if(self.title != ""):
			ret_string = ret_string + self.title + ": "
		if(self.subject != ""):
			ret_string = ret_string + self.subject + " "
		if(self.type != ""):
			ret_string = ret_string + self.type + " "
		if(self.level != ""):
			ret_string = ret_string + "Level " + self.level + " "
		if(self.quality != ""):
			ret_string = ret_string + "Quality " + self.quality + " "
		if(self.value != ""):
			ret_string = ret_string + "(" + self.value + "bp) "
		return ret_string

	def __lt__(self, other):
		if(isart(self.subject) and not isart(other.subject)):
			return True
		elif(not isart(self.subject) and isart(other.subject)):
			return False
		else:
			if(self.subject == other.subject):
				return self.title < other.title
			else:
				return self.subject < other.subject

		
#book names

generic = ["On ","A Treatise on ","Regarding ","Investigations of ","Collected Correspondences on ","Notes on ","Commentary regarding ","An exploration of ","Book of ","Thoughts on ","Thoughts regarding ","Of ","Regarding ","Wisdom regarding ","A Discussion of "]

#arts

animal_high = ["Comparative Anatomy Volume I","Ursula's 'On Nature' Book III","Ursula's 'On Nature' Book IV","The Rugen Bestiary","Nobility Among Beasts"]
animal_medium = ["Comparative Anatomy Volume I (damaged)","Ursula's 'On Nature' Book III (damaged)","Ursula's 'On Nature' Book IV (damaged)","Hermetic Bestiary","On Mastery over Beasts","Fundamentals of Animal","On the Birds of the Greek Islands","The Rugen Bestiary (damaged)","Canine Anatomy","Nobility Among Beasts (damaged)"]
animal_low = ["On the Categories of Beast","On Fish","On Birds","Hermetic Bestiary (damaged)","On Mastery over Beasts (damaged)","Cats and how they Torment their Masters","Fundamentals of Animal (damaged)","On the Virtues of Sheep","Canine Anatomy (damaged)"]

creo_high = ["Juliasta's 'Commentaries on Anaximander I - Apeiron as Generative Principle'"]
creo_medium = ["Juliasta's 'Commentaries on Anaximander I - Apeiron as Generative Principle' (damaged)"]
creo_low = ["Collected Correspondences on Creo"]

corpus_high = ["The Humors and their Relation to the Form of Corpus","On the Structures of the Human Body","On the Destruction and Repair of the Senses","On the Devising of Longevity Rituals","On the Healing of Wounds","On the Healing of Bones","Of Flesh","Comparative Anatomy Volume II","The Substance of Man"]
corpus_medium = ["The Humors and their Relation to the Form of Corpus (damaged)","On the Structures of the Human Body (damaged)","On the Destruction and Repair of the Senses (damaged)","On the Animation of Corpses","On the Devising of Longevity Rituals (damaged)","On the Vital Faculty","On the Healing of Wounds (damaged)","On the Healing of Bones","A Hermetic Study of the Lungs and Heart I","A Hermetic Study of the Lungs and Heart II","Of Flesh (damaged)","Comparative Anatomy Volume II (damaged)","The Substance of Man (damaged)","Vulnerabilities of the Human Form"]
corpus_low = ["Cantations for Health and Hygeine","Collected Correspondences on Corpus","On the Animation of Corpses (damaged)","On the Vital Faculty (damaged)","Methods for Preservation of the Dead","A Hermetic Study of the Lungs and Heart I (damaged)","A Hermetic Study of the Lungs and Heart II (damaged)","Vulnerabilities of the Human Form (damaged)"]

herbam_high = ["Ursula's 'On Nature' Book II"]

ignem_high = ["Crossing the Phlegethon","Flame Seen and Unseen","Elaine filia Flambeau's 'On Ignem'","Apromor filius Flambeau's 'Against Ignem' Book I"]
ignem_medium = ["Crossing the Phlegethon (damaged)","On the Igneous Properties of Various Woods","Collected Sayings of Flambeau","Fragments of Heraclitus' On Nature","Flame Seen and Unseen (damaged)","Elaine filia Flambeau's 'On Fire' (damaged)","Apromor filius Flambeau's 'Against Ignem' Book I (damaged)"]
ignem_low = ["On the Igneous Properties of Various Woods (damaged)","Collected Sayings of Flambeau (damaged)","Collected Correspondences on Ignem","Fragments of Heraclitus' On Nature (damaged)","In Search of the Phoenix"]

mentem_high = ["On the Structures of the Mind","On Reason","Translation and Commentary of Aristotle's 'On the Soul'","On the Interrelation of Mind, Spirit, and Soul","Tremere's 'Fetid Wisdom'","Kore's 'On Necromancy' Volume I","Kore's 'On Necromancy' Volume III","Kore's 'On Necromancy' Volume IV"]
mentem_medium = ["On the Structures of the Mind (damaged)","On Reason (damaged)","Translation and Commentary of Aristotle's 'On the Soul' (damaged)","On the Interrelation of Mind, Spirit, and Soul (damaged)","Tremere's 'Certamen'","Kore's 'On Necromancy' Volume I (damaged)","Kore's 'On Necromancy' Volume III (damaged)","Kore's 'On Necromancy' Volume IV (damaged)","Lives of the Dead","Ursula's 'On Nature' Book V"]
mentem_low = ["Collected Correspondences on Mentem","Riddles for the Apprentice","Contemplations","Tremere's 'Certamen' (damaged)","Ghost Stories for Apprentices","On Ethereal Beings","A Study of Ethereal Fishermen Spiders","Lives of the Dead (damaged)","Ursula's 'On Nature' Book V (damaged)"]

muto_high = ["Juliasta's 'Commentaries on Anaximander IV - The Evolution of Man from Fish'"]
muto_medium = ["Juliasta's 'Commentaries on Anaximander IV - The Evolution of Man from Fish' (damaged)"]
muto_low = ["Collected Correspondences on Muto"]

perdo_high = ["Juliasta's 'Commentaries on Anaximander II - Apeiron as Degenerative Principle'","Apromor filius Flambeau's 'Against Ignem' Book II","Apromor filius Flambeau's 'Against Ignem' Book III"]
perdo_medium = ["Juliasta's 'Commentaries on Anaximander II - Apeiron as Degenerative Principle' (damaged)","Apromor filius Flambeau's 'Against Ignem' Book II (damaged)","Apromor filius Flambeau's 'Against Ignem' Book III (damaged)"]
perdo_low = ["Collected Correspondences on Perdo"]

rego_high = ["Kore's 'On Necromancy' Volume II","Kore's 'On Necromancy' Volume V","Kore's 'On Necromancy' Volume VI"]

vim_high = ["On the Properties of Fluid Vis","Kore's 'On Necromancy' Volume VII"]
vim_medium = ["Pseudo-Juliasta's 'Commentaries on Anaximander III - The Mystical Properties of Apeiron'","Conciatta's 'The Application of Vim to the Supernatural Humors'","On the Properties of Fluid Vis (damaged)"]
vim_low = ["Pseudo-Juliasta's 'Commentaries on Anaximander III - The Mystical Properties of Apeiron' (damaged)","Conciatta's 'The Application of Vim to the Supernatural Humors' (damaged)"]

#abilities

chirurgy_high = ["An Excerpt from the Hippocratic Corpus in Greek","Hippocrates' 'On Fractures'","Hippocrates' 'On Injuries of the Head'","Hippocrates' 'On Joints'"]
chirurgy_medium = ["An Excerpt from the Hippocratic Corpus in Greek (damaged)","An Excerpt from the Hippocratic Corpus in Latin","Hippocrates' 'On Fractures' (damaged)","Hippocrates' 'On Injuries of the Head' (damaged)","Hippocrates' 'On Joints' (damaged)"]
chirurgy_low = ["An Excerpt from the Hippocratic Corpus in Latin (damaged)"]

magic_lore_high = ["Juliasta's 'Commentaries on Anaximander III - The Mystical Properties of Apeiron'","The Prophecies of Merlin","A Survey of Magical Beasts Found in Nature","Architrenius","Physiologus","Ursula's 'On Nature' Book I"]
magic_lore_medium = ["Juliasta's 'Commentaries on Anaximander III - The Mystical Properties of Apeiron' (damaged)","The Prophecies of Merlin (damaged)","A Survey of Magical Beasts Found in Nature (damaged)","Architrenius (damaged)","Ovid's 'Metamorphoses'","Physiologus (damaged)","Otto Pauel's 'Journal of Unusual Encounters' Book IV","The Wisdom of Fionntan","Ursula's 'On Nature' Book I (damaged)"]
magic_lore_low = ["Unusual Beasts and How to Avoid Them","Ovid's 'Metamorphoses' (damaged)","Otto Pauel's 'Journal of Unusual Encounters' Book IV (damaged)","The Wisdom of Fionntan (damaged)"]
	
medicine_high = ["An Excerpt from the Hippocratic Corpus in Greek","Hippocrates' 'On Airs, Waters, and Places'","Hippocrates' 'On the Diseases of Women'","Hippocrates' 'On Epidemics' Book I","Hippocrates' 'On Epidemics' Book III"]
medicine_medium = ["An Excerpt from the Hippocratic Corpus in Greek (damaged)","An Excerpt from the Hippocratic Corpus in Latin","Hippocrates' 'On Airs, Waters, and Places' (damaged)","On the Sacred Disease","Hippocrates' 'On the Diseases of Women' (damaged)","Hippocrates' 'On Epidemics' Book II","Hippocrates' 'On Epidemics' Book I (damaged)","Hippocrates' 'On Epidemics' Book III (damaged)"]
medicine_low = ["An Excerpt from the Hippocratic Corpus in Latin (damaged)","On the Sacred Disease (damaged)","Hippocrates' 'On Epidemics' Book II (damaged)"]

music_high = ["Boethius' 'On Music'","Johannes Cotto's 'On Music'","Guido d'Arezzo's 'Micrologus'"]
music_medium = ["Boethius' 'On Music' (damaged)","Aurelianus Reomensis' 'Disipline of Music'","Johannes Cotto's 'On Music' (damaged)","Guido d'Arezzo's 'Micrologus' (damaged)"]
music_low = ["An Excerpt from the Hippocratic Corpus in Latin (damaged)","On the Sacred Disease (damaged)","Hippocrates' 'On Epidemics' Book II (damaged)","Aurelianus Reomensis' 'Disipline of Music' (damaged)","On the Composition of Motets"]

parma_magica_high = ["Bonisagus' 'Parma Magica'","Notatus' 'Commentaries on Parma Magica'","That Which Was Shared"]
parma_magica_medium = ["Bonisagus' 'Parma Magica' (damaged)","Bonisagus' 'Parma Magica' (abridged)","That Which Was Shared (damaged)","Variants of the Parma Magica","Shield of the Mighty","Investigations into Aligning Parma Magica to Specific Forms"]
parma_magica_low = ["Variants of the Parma Magica (damaged)","A Refinement of the Parma Magica","Shield of the Mighty (damaged)","Investigations into Aligning Parma Magica to Specific Forms (damaged)"]
	
#this function calculates the bp value of the passed book object, b
def evaluate(b):

	bp_value = 0
	#tractatus
	if(b.type == "Tractatus"):
		bp_value = bp_value + int(b.quality)
	#summa
	else:
		#is art summa
		if(isart(b.subject)):
			bp_value = bp_value + int(b.quality) + int(b.level)
		else:
			bp_value = bp_value + ((int(b.quality) + int(b.level))*3)
			
	return bp_value
	
#this function contains lists of names for books on various topics
#they are split up based on level and quality for some internal consistency
def name_book(topic,level,quality):

	#if none of the options get triggered we just return a blank string
	ret_string = ""
	
	#give it a generic name that gets replaced by a more specific one if the topic matches one of the categories
	ret_string = generic[random.randint(0,len(generic)-1)] + topic

	if(topic == "Animal"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(animal_high)>0):
					r = random.randint(0,len(animal_high)-1)
					ret_string = animal_high[r]
					#delete the name to avoid duplicates
					del animal_high[r]
			elif(quality > 4):
				#medium
				if(len(animal_medium)>0):
					r = random.randint(0,len(animal_medium)-1)
					ret_string = animal_medium[r]
					#delete the name to avoid duplicates
					del animal_medium[r]
			else:
				#low
				if(len(animal_low)>0):
					r = random.randint(0,len(animal_low)-1)
					ret_string = animal_low[r]
					#delete the name to avoid duplicates
					del animal_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(animal_high)>0):
					r = random.randint(0,len(animal_high)-1)
					ret_string = animal_high[r]
					#delete the name to avoid duplicates
					del animal_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(animal_medium)>0):
					r = random.randint(0,len(animal_medium)-1)
					ret_string = animal_medium[r]
					#delete the name to avoid duplicates
					del animal_medium[r]
			else: 
				#low
				if(len(animal_low)>0):
					r = random.randint(0,len(animal_low)-1)
					ret_string = animal_low[r]
					#delete the name to avoid duplicates
					del animal_low[r]
					
	
	if(topic == "Creo"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(creo_high)>0):
					r = random.randint(0,len(creo_high)-1)
					ret_string = creo_high[r]
					#delete the name to avoid duplicates
					del creo_high[r]
			elif(quality > 4):
				#medium
				if(len(creo_medium)>0):
					r = random.randint(0,len(creo_medium)-1)
					ret_string = creo_medium[r]
					#delete the name to avoid duplicates
					del creo_medium[r]
			else:
				#low
				if(len(creo_low)>0):
					r = random.randint(0,len(creo_low)-1)
					ret_string = creo_low[r]
					#delete the name to avoid duplicates
					del creo_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(creo_high)>0):
					r = random.randint(0,len(creo_high)-1)
					ret_string = creo_high[r]
					#delete the name to avoid duplicates
					del creo_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(creo_medium)>0):
					r = random.randint(0,len(creo_medium)-1)
					ret_string = creo_medium[r]
					#delete the name to avoid duplicates
					del creo_medium[r]
			else: 
				#low
				if(len(creo_low)>0):
					r = random.randint(0,len(creo_low)-1)
					ret_string = creo_low[r]
					#delete the name to avoid duplicates
					del creo_low[r]
	
	if(topic == "Corpus"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(corpus_high)>0):
					r = random.randint(0,len(corpus_high)-1)
					ret_string = corpus_high[r]
					#delete the name to avoid duplicates
					del corpus_high[r]
			elif(quality > 4):
				#medium
				if(len(corpus_medium)>0):
					r = random.randint(0,len(corpus_medium)-1)
					ret_string = corpus_medium[r]
					#delete the name to avoid duplicates
					del corpus_medium[r]
			else:
				#low
				if(len(corpus_low)>0):
					r = random.randint(0,len(corpus_low)-1)
					ret_string = corpus_low[r]
					#delete the name to avoid duplicates
					del corpus_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(corpus_high)>0):
					r = random.randint(0,len(corpus_high)-1)
					ret_string = corpus_high[r]
					#delete the name to avoid duplicates
					del corpus_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(corpus_medium)>0):
					r = random.randint(0,len(corpus_medium)-1)
					ret_string = corpus_medium[r]
					#delete the name to avoid duplicates
					del corpus_medium[r]
			else: 
				#low
				if(len(corpus_low)>0):
					r = random.randint(0,len(corpus_low)-1)
					ret_string = corpus_low[r]
					#delete the name to avoid duplicates
					del corpus_low[r]
	
	
	if(topic == "Ignem"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(ignem_high)>0):
					r = random.randint(0,len(ignem_high)-1)
					ret_string = ignem_high[r]
					#delete the name to avoid duplicates
					del ignem_high[r]
			elif(quality > 4):
				#medium
				if(len(ignem_medium)>0):
					r = random.randint(0,len(ignem_medium)-1)
					ret_string = ignem_medium[r]
					#delete the name to avoid duplicates
					del ignem_medium[r]
			else:
				#low
				if(len(ignem_low)>0):
					r = random.randint(0,len(ignem_low)-1)
					ret_string = ignem_low[r]
					#delete the name to avoid duplicates
					del ignem_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(ignem_high)>0):
					r = random.randint(0,len(ignem_high)-1)
					ret_string = ignem_high[r]
					#delete the name to avoid duplicates
					del ignem_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(ignem_medium)>0):
					r = random.randint(0,len(ignem_medium)-1)
					ret_string = ignem_medium[r]
					#delete the name to avoid duplicates
					del ignem_medium[r]
			else: 
				#low
				if(len(ignem_low)>0):
					r = random.randint(0,len(ignem_low)-1)
					ret_string = ignem_low[r]
					#delete the name to avoid duplicates
					del ignem_low[r]
					
	if(topic == "Mentem"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(mentem_high)>0):
					r = random.randint(0,len(mentem_high)-1)
					ret_string = mentem_high[r]
					#delete the name to avoid duplicates
					del mentem_high[r]
			elif(quality > 4):
				#medium
				if(len(mentem_medium)>0):
					r = random.randint(0,len(mentem_medium)-1)
					ret_string = mentem_medium[r]
					#delete the name to avoid duplicates
					del mentem_medium[r]
			else:
				#low
				if(len(mentem_low)>0):
					r = random.randint(0,len(mentem_low)-1)
					ret_string = mentem_low[r]
					#delete the name to avoid duplicates
					del mentem_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(mentem_high)>0):
					r = random.randint(0,len(mentem_high)-1)
					ret_string = mentem_high[r]
					#delete the name to avoid duplicates
					del mentem_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(mentem_medium)>0):
					r = random.randint(0,len(mentem_medium)-1)
					ret_string = mentem_medium[r]
					#delete the name to avoid duplicates
					del mentem_medium[r]
			else: 
				#low
				if(len(mentem_low)>0):
					r = random.randint(0,len(mentem_low)-1)
					ret_string = mentem_low[r]
					#delete the name to avoid duplicates
					del mentem_low[r]
					
					
	if(topic == "Muto"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(muto_high)>0):
					r = random.randint(0,len(muto_high)-1)
					ret_string = muto_high[r]
					#delete the name to avoid duplicates
					del muto_high[r]
			elif(quality > 4):
				#medium
				if(len(muto_medium)>0):
					r = random.randint(0,len(muto_medium)-1)
					ret_string = muto_medium[r]
					#delete the name to avoid duplicates
					del muto_medium[r]
			else:
				#low
				if(len(muto_low)>0):
					r = random.randint(0,len(muto_low)-1)
					ret_string = muto_low[r]
					#delete the name to avoid duplicates
					del muto_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(muto_high)>0):
					r = random.randint(0,len(muto_high)-1)
					ret_string = muto_high[r]
					#delete the name to avoid duplicates
					del muto_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(muto_medium)>0):
					r = random.randint(0,len(muto_medium)-1)
					ret_string = muto_medium[r]
					#delete the name to avoid duplicates
					del muto_medium[r]
			else: 
				#low
				if(len(muto_low)>0):
					r = random.randint(0,len(muto_low)-1)
					ret_string = muto_low[r]
					#delete the name to avoid duplicates
					del muto_low[r]
	
	if(topic == "Perdo"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(perdo_high)>0):
					r = random.randint(0,len(perdo_high)-1)
					ret_string = perdo_high[r]
					#delete the name to avoid duplicates
					del perdo_high[r]
			elif(quality > 4):
				#medium
				if(len(perdo_medium)>0):
					r = random.randint(0,len(perdo_medium)-1)
					ret_string = perdo_medium[r]
					#delete the name to avoid duplicates
					del perdo_medium[r]
			else:
				#low
				if(len(perdo_low)>0):
					r = random.randint(0,len(perdo_low)-1)
					ret_string = perdo_low[r]
					#delete the name to avoid duplicates
					del perdo_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(perdo_high)>0):
					r = random.randint(0,len(perdo_high)-1)
					ret_string = perdo_high[r]
					#delete the name to avoid duplicates
					del perdo_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(perdo_medium)>0):
					r = random.randint(0,len(perdo_medium)-1)
					ret_string = perdo_medium[r]
					#delete the name to avoid duplicates
					del perdo_medium[r]
			else: 
				#low
				if(len(perdo_low)>0):
					r = random.randint(0,len(perdo_low)-1)
					ret_string = perdo_low[r]
					#delete the name to avoid duplicates
					del perdo_low[r]
				
	if(topic == "Vim"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(vim_high)>0):
					r = random.randint(0,len(vim_high)-1)
					ret_string = vim_high[r]
					#delete the name to avoid duplicates
					del vim_high[r]
			elif(quality > 4):
				#medium
				if(len(vim_medium)>0):
					r = random.randint(0,len(vim_medium)-1)
					ret_string = vim_medium[r]
					#delete the name to avoid duplicates
					del vim_medium[r]
			else:
				#low
				if(len(vim_low)>0):
					r = random.randint(0,len(vim_low)-1)
					ret_string = vim_low[r]
					#delete the name to avoid duplicates
					del vim_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(vim_high)>0):
					r = random.randint(0,len(vim_high)-1)
					ret_string = vim_high[r]
					#delete the name to avoid duplicates
					del vim_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(vim_medium)>0):
					r = random.randint(0,len(vim_medium)-1)
					ret_string = vim_medium[r]
					#delete the name to avoid duplicates
					del vim_medium[r]
			else: 
				#low
				if(len(vim_low)>0):
					r = random.randint(0,len(vim_low)-1)
					ret_string = vim_low[r]
					#delete the name to avoid duplicates
					del vim_low[r]
	
	#abilities
	if(topic == "Magic Lore"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(magic_lore_high)>0):
					r = random.randint(0,len(magic_lore_high)-1)
					ret_string = magic_lore_high[r]
					#delete the name to avoid duplicates
					del magic_lore_high[r]
			elif(quality > 4):
				#medium
				if(len(magic_lore_medium)>0):
					r = random.randint(0,len(magic_lore_medium)-1)
					ret_string = magic_lore_medium[r]
					#delete the name to avoid duplicates
					del magic_lore_medium[r]
			else:
				#low
				if(len(magic_lore_low)>0):
					r = random.randint(0,len(magic_lore_low)-1)
					ret_string = magic_lore_low[r]
					#delete the name to avoid duplicates
					del magic_lore_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(magic_lore_high)>0):
					r = random.randint(0,len(magic_lore_high)-1)
					ret_string = magic_lore_high[r]
					#delete the name to avoid duplicates
					del magic_lore_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(magic_lore_medium)>0):
					r = random.randint(0,len(magic_lore_medium)-1)
					ret_string = magic_lore_medium[r]
					#delete the name to avoid duplicates
					del magic_lore_medium[r]
			else: 
				#low
				if(len(magic_lore_low)>0):
					r = random.randint(0,len(magic_lore_low)-1)
					ret_string = magic_lore_low[r]
					#delete the name to avoid duplicates
					del magic_lore_low[r]
	
	if(topic == "Chirurgy"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(chirurgy_high)>0):
					r = random.randint(0,len(chirurgy_high)-1)
					ret_string = chirurgy_high[r]
					#delete the name to avoid duplicates
					del chirurgy_high[r]
			elif(quality > 4):
				#medium
				if(len(chirurgy_medium)>0):
					r = random.randint(0,len(chirurgy_medium)-1)
					ret_string = chirurgy_medium[r]
					#delete the name to avoid duplicates
					del chirurgy_medium[r]
			else:
				#low
				if(len(chirurgy_low)>0):
					r = random.randint(0,len(chirurgy_low)-1)
					ret_string = chirurgy_low[r]
					#delete the name to avoid duplicates
					del chirurgy_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(chirurgy_high)>0):
					r = random.randint(0,len(chirurgy_high)-1)
					ret_string = chirurgy_high[r]
					#delete the name to avoid duplicates
					del chirurgy_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(chirurgy_medium)>0):
					r = random.randint(0,len(chirurgy_medium)-1)
					ret_string = chirurgy_medium[r]
					#delete the name to avoid duplicates
					del chirurgy_medium[r]
			else: 
				#low
				if(len(chirurgy_low)>0):
					r = random.randint(0,len(chirurgy_low)-1)
					ret_string = chirurgy_low[r]
					#delete the name to avoid duplicates
					del chirurgy_low[r]
	
	if(topic == "Medicine"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(medicine_high)>0):
					r = random.randint(0,len(medicine_high)-1)
					ret_string = medicine_high[r]
					#delete the name to avoid duplicates
					del medicine_high[r]
			elif(quality > 4):
				#medium
				if(len(medicine_medium)>0):
					r = random.randint(0,len(medicine_medium)-1)
					ret_string = medicine_medium[r]
					#delete the name to avoid duplicates
					del medicine_medium[r]
			else:
				#low
				if(len(medicine_low)>0):
					r = random.randint(0,len(medicine_low)-1)
					ret_string = medicine_low[r]
					#delete the name to avoid duplicates
					del medicine_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(medicine_high)>0):
					r = random.randint(0,len(medicine_high)-1)
					ret_string = medicine_high[r]
					#delete the name to avoid duplicates
					del medicine_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(medicine_medium)>0):
					r = random.randint(0,len(medicine_medium)-1)
					ret_string = medicine_medium[r]
					#delete the name to avoid duplicates
					del medicine_medium[r]
			else: 
				#low
				if(len(medicine_low)>0):
					r = random.randint(0,len(medicine_low)-1)
					ret_string = medicine_low[r]
					#delete the name to avoid duplicates
					del medicine_low[r]
	
	if(topic == "Parma Magica"):
		#tractatus
		if(level == 0):
			if(quality > 7):
				#high
				if(len(parma_magica_high)>0):
					r = random.randint(0,len(parma_magica_high)-1)
					ret_string = parma_magica_high[r]
					#delete the name to avoid duplicates
					del parma_magica_high[r]
			elif(quality > 4):
				#medium
				if(len(parma_magica_medium)>0):
					r = random.randint(0,len(parma_magica_medium)-1)
					ret_string = parma_magica_medium[r]
					#delete the name to avoid duplicates
					del parma_magica_medium[r]
			else:
				#low
				if(len(parma_magica_low)>0):
					r = random.randint(0,len(parma_magica_low)-1)
					ret_string = parma_magica_low[r]
					#delete the name to avoid duplicates
					del parma_magica_low[r]
		else:
			if((level+quality) > 22):
				#high
				if(len(parma_magica_high)>0):
					r = random.randint(0,len(parma_magica_high)-1)
					ret_string = parma_magica_high[r]
					#delete the name to avoid duplicates
					del parma_magica_high[r]
			elif((level+quality) > 11):
				#medium
				if(len(parma_magica_medium)>0):
					r = random.randint(0,len(parma_magica_medium)-1)
					ret_string = parma_magica_medium[r]
					#delete the name to avoid duplicates
					del parma_magica_medium[r]
			else: 
				#low
				if(len(parma_magica_low)>0):
					r = random.randint(0,len(parma_magica_low)-1)
					ret_string = parma_magica_low[r]
					#delete the name to avoid duplicates
					del parma_magica_low[r]
	
	return ret_string
	
#this is where we keep the book objects
library = []

#which book in the library is open in the scriptorium as an index of the library list
scriptorium_index = 0;
	
#lists	
arts_list = ["Creo","Intellego","Muto","Perdo","Rego","Animal","Aquam","Auram","Corpus","Herbam","Ignem","Imaginem","Mentem","Terram","Vim"]
techniques_list = ["Creo","Intellego","Muto","Perdo","Rego"]
forms_list = ["Animal","Aquam","Auram","Corpus","Herbam","Ignem","Imaginem","Mentem","Terram","Vim"]

childhood_abilities = ["Athletics", "Awareness", "Brawl", "Charm", "Folk Ken", "Guile", "Second Language", "Stealth", "Survival", "Swim"]
general_abilities = ["Animal Handling","Area Lore (Homeland)","Area Lores (Other)","Athletics","Awareness","Bargain","Brawl","Carouse","Charm","Chirurgy","Concentration","Craft (Type)","Etiquette","Folk Ken","Guile","Hunt","Intrigue","Leadership","Legerdemain","Native Language","Languages (Other)","Music","Organisation Lores (Other)","Profession (Type)","Ride","Stealth","Survival","Swim","Teaching"]
arcane_abilities = ["Code of Hermes","Dominion Lore","Faerie Lore","Finesse","Infernal Lore","Magic Lore","Magic Theory","Parma Magica","Penetration"]
hermetic_favoured_abilities = ["Code of Hermes","Dominion Lore","Faerie Lore","Finesse","Infernal Lore","Magic Lore","Magic Theory","Order of Hermes Lore","Parma Magica","Penetration"]
academic_abilities = []
martial_abilities = ["Bows","Great Weapon","Single Weapon","Thrown Weapon"]
supernatural_abilities = []
favoured_topics = ["Magic Theory"]
all_abilities = general_abilities + arcane_abilities + academic_abilities + martial_abilities + supernatural_abilities
	
#the number of build points worth of stuff to generate	
bp = 0
	
#whether we're generating a summa or tractatus	
summa = False

#if it is a summa this determines if it is an art or ability summa. 0 = art, 1 = ability
summa_type = 0

#the level of a summa
summa_level = 0

#quality
quality = 0
tractatus_min_quality = 1
tractatus_max_quality = 11

#upper limit for randomly generated quality
qlimit = 0

#topic the book covers
topic = "Oops, something went wrong if you see this!"

def picktopic():
	#50% chance of being on a favoured topic, skip if favoured list is empty
	if((random.randint(0,1) == 0) and (len(favoured_topics) > 0) and (favoured_topics[0] != "")):
		#favoured
		topic = favoured_topics[random.randint(0,len(favoured_topics)-1)]
	else:
		#otherwise 50% chance of art vs ability
		if(random.randint(0,1) == 0):
			#art
			topic = arts_list[random.randint(0,14)]
		else:
			#there is a 50/50 chance that a hermetic ability book is on one of hermetic_favoured_abilities, otherwise it's a completely random one chosen from all abilities
			if(random.randint(0,1) == 0):
				topic = hermetic_favoured_abilities[random.randint(0,len(hermetic_favoured_abilities)-1)]
			else:
				topic = all_abilities[random.randint(0,len(all_abilities)-1)]
			
	print(favoured_topics)
	print(topic)
	return topic

def bookgen():

	bp = 0
	total_bp = 0
	global library
	global tractatus_min_quality 
	tractatus_min_quality = int(entry_tractatus_min_quality.get())
	global tractatus_max_quality 
	tractatus_max_quality = int(entry_tractatus_max_quality.get())
	global favoured_topics
	favoured_topics = entry_favoured_topics.get("1.0","end").strip().split(',')
	#library = []

	try:
		bp = int(entry_unused_bp.get())
	except:
		print("ERROR: NaN")
	
	if(bp > 0):
		
		#read the current total
		try:
			total_bp = int(entry_total_bp.get())
		except:
			print("ERROR: NaN")
			
		total_bp = total_bp + bp
		
		entry_total_bp.config(state= "normal")
		entry_total_bp.delete('0','end')
		entry_total_bp.insert('0',str(total_bp))
		entry_total_bp.config(state= "disabled")
		
		entry_unused_bp.delete('0','end')
		entry_unused_bp.insert('0','0')
		
		#the main loop, generate books and add to the library list until all the bp are used
		while bp > 0:
			#pick topic
			topic = picktopic()
			#summa or tractatus? Coin flip
			if(random.randint(0,1) == 0):
				#summa
				summa = True
				if(isart(topic)):
					#randomly generate a level, cap is 20 for an art summa as per Covenants pg. 5
					summa_level = random.randint(1,20)
					#art summa quality limit is 11+(20-level) or 22 if that is lower
					if(summa_level < 10):
						qlimit = 22
					else:
						qlimit = 11+(20-summa_level)
					quality = random.randint(1,qlimit)
					library.append(Book("Summa",name_book(topic,summa_level,quality),topic,str(quality),str(summa_level),"",""))
					#modify bp now that we've added a book
					bp = bp - (quality+summa_level)
				else:
					#randomly generate a level, cap is 8 for an ability summa as per Covenants pg. 5
					summa_level = random.randint(1,8)
					#ability summa quality limit is 11+(3x(8-level)) or 22 if that is lower
					if(summa_level < 4):
						qlimit = 22
					else:
						qlimit = 11+(3*(8-summa_level))
					quality = random.randint(1,qlimit)
					library.append(Book("Summa",name_book(topic,summa_level,quality),topic,str(quality),str(summa_level),"",""))
					#modify bp now that we've added a book
					bp = bp - 3*((quality+summa_level))	
				
			else:
				#tractatus
				summa = False
				if(isart(topic)):
					quality = random.randint(tractatus_min_quality,tractatus_max_quality)
					library.append(Book("Tractatus",name_book(topic,0,quality),topic,str(quality),"","",""))
					#modify bp now that we've added a book
					bp = bp - quality
				else:
					quality = random.randint(tractatus_min_quality,tractatus_max_quality)
					library.append(Book("Tractatus",name_book(topic,0,quality),topic,str(quality),"","",""))
					#modify bp now that we've added a book
					bp = bp - quality

		#after the loop print the library
		
		library.sort()
		
		libstring = ""
		
		for b in library:
			b.value = str(evaluate(b))
			libstring = libstring + b.getDescription() + "\n"
			
		entry_library_contents.delete('1.0','end')
		entry_library_contents.insert('1.0',libstring)

def savelib():
	file = filedialog.asksaveasfilename(initialdir="/", title="Save file",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
	global library
	with open(file,'w') as f:
		for b in library:
			#type,title,subject,quality,level
			wstr = b.type + "|" + b.title + "|" + b.subject + "|" + b.quality + "|"
			if(b.level == ""):
				wstr = wstr + "X" + "|"
			else:
				wstr = wstr + b.level + "|"
			wstr = wstr + b.desc + "|" + b.value + "\n"
			f.write(wstr)
	f.close()
	#print(path)

#calculates the bp value of the whole library
def calculate_cost():
	global library
	bp_value = 0
	for b in library:
		#tractatus
		if(b.type == "Tractatus"):
			bp_value = bp_value + int(b.quality)
		#summa
		else:
			#is art summa
			if(isart(b.subject)):
				bp_value = bp_value + int(b.quality) + int(b.level)
			else:
				bp_value = bp_value + ((int(b.quality) + int(b.level))*3)
				
	entry_total_bp.config(state= "normal")
	entry_total_bp.delete('0','end')
	entry_total_bp.insert('0',str(bp_value))
	entry_total_bp.config(state= "disabled")
	
def loadlib():
	file = filedialog.askopenfilename(initialdir="/", title="Load file",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
	global library
	library.clear()
	libstring = ""
	bp_value = 0
	with open(file,'r') as f:
		for line in f:
			lblist = line.strip().split('|')
			#tractatus
			if(lblist[4] == 'X'):
				library.append(Book(lblist[0],lblist[1],lblist[2],lblist[3],"",lblist[5],lblist[6]))
				bp_value = bp_value + int(lblist[3])
			#summa
			else:
				library.append(Book(lblist[0],lblist[1],lblist[2],lblist[3],lblist[4],lblist[5],lblist[6]))
				#is art summa
				if(lblist[2] == "Creo" or lblist[2] == "Muto" or lblist[2] == "Intellego" or lblist[2] == "Perdo" or lblist[2] == "Rego" or lblist[2] == "Animal" or lblist[2] == "Aquam" or lblist[2] == "Auram" or lblist[2] == "Corpus" or lblist[2] == "Ignem" or lblist[2] == "Imaginem" or lblist[2] == "Terram" or lblist[2] == "Vim" or lblist[2] == "Mentem"):
					bp_value = bp_value + int(lblist[3]) + int(lblist[4])
				else:
					bp_value = bp_value + ((int(lblist[3]) + int(lblist[4]))*3)

			
	f.close()
	
	entry_total_bp.config(state= "normal")
	entry_total_bp.delete('0','end')
	entry_total_bp.insert('0',str(bp_value))
	entry_total_bp.config(state= "disabled")
	
	book_name_list = ["Create New"]
	
	for b in library:
		libstring = libstring + b.getDescription() + "\n"
		book_name_list.append(b.title)
		
	book_list_select['values'] = book_name_list
		
	entry_library_contents.delete('1.0','end')
	entry_library_contents.insert('1.0',libstring)
	
def displaylib():
	global library
	
	libstring = ""
	
	for b in library:
		libstring = libstring + b.getDescription() + "\n"
		
	entry_library_contents.delete('1.0','end')
	entry_library_contents.insert('1.0',libstring)
	
def find_book_by_name(name):
	
	ret_val = Book("","","","","","","")
	global library 
	for b in library:
		print(b.title)
		if(b.title == name):
			ret_val = b
	
	print(ret_val.title)
	
	return ret_val
	
def populate_scriptorium(event):
	print("Combobox event")
	global library
	global scriptorium_index
	book_name = book_list_select.get()
	scriptorium_index = book_list_select.current()-1
	print(book_name)
	if(book_name == "Create New"):
		#clear boxes
		entry_scriptorium_title.delete('1.0','end')
		entry_scriptorium_type.delete('0','end')
		entry_scriptorium_subject.delete('0','end')
		entry_scriptorium_quality.delete('0','end')
		entry_scriptorium_level.config(state= "normal")
		entry_scriptorium_level.delete('0','end')
	else:
		#populate boxes with info
		#book_obj = find_book_by_name(book_name.strip())
		book_obj = library[scriptorium_index]
		print(book_obj.title)
		entry_scriptorium_title.delete('1.0','end')
		entry_scriptorium_title.insert('1.0',book_obj.title)
		entry_scriptorium_type.delete('0','end')
		entry_scriptorium_type.insert('0',book_obj.type)
		entry_scriptorium_subject.delete('0','end')
		entry_scriptorium_subject.insert('0',book_obj.subject)
		entry_scriptorium_quality.delete('0','end')
		entry_scriptorium_quality.insert('0',book_obj.quality)
		entry_scriptorium_level.config(state= "normal")
		entry_scriptorium_level.delete('0','end')
		entry_scriptorium_level.insert('0',book_obj.level)
		if(book_obj.type == "Tractatus"):
			entry_scriptorium_level.config(state= "disabled")
			
def isart(name):
	if(name == "Creo" or name == "Muto" or name == "Intellego" or name == "Perdo" or name == "Rego" or name == "Animal" or name == "Aquam" or name == "Auram" or name == "Corpus" or name == "Ignem" or name == "Imaginem" or name == "Terram" or name == "Vim" or name == "Mentem" or name == "Herbam"):
		return True
	else:
		return False
		
def savebook():
	global scriptorium_index
	global library
	if(book_list_select.current() == 0):
		book_obj = Book("","","","","")
		book_obj.title = entry_scriptorium_title.get('1.0','end').strip()
		book_obj.type = entry_scriptorium_type.get()
		book_obj.subject = entry_scriptorium_subject.get()
		book_obj.quality = entry_scriptorium_quality.get()
		book_obj.level = entry_scriptorium_level.get()
		book_obj.desc = entry_scriptorium_description.get('1.0','end').strip()
		library.append(book_obj)
		scriptorium_index = len(library)-1
	else:
		book_obj = library[scriptorium_index]
		book_obj.title = entry_scriptorium_title.get('1.0','end').strip()
		book_obj.type = entry_scriptorium_type.get()
		book_obj.subject = entry_scriptorium_subject.get()
		book_obj.quality = entry_scriptorium_quality.get()
		book_obj.level = entry_scriptorium_level.get()
		library[scriptorium_index] = book_obj
		
		
	calculate_cost()
	
	libstring = ""
	
	book_name_list = ["Create New"]
	
	for b in library:
		libstring = libstring + b.getDescription() + "\n"
		book_name_list.append(b.title)
		
	book_list_select['values'] = book_name_list
	book_list_select.current(scriptorium_index+1)
	
	displaylib()
		
	
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1368x900")
window.configure(bg = "#AB977A")


canvas = Canvas(
    window,
    bg = "#AB977A",
    height = 900,
    width = 1368,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    142.0,
    136.0,
    293.0,
    166.0,
    fill="#A73E3E",
    outline="")

canvas.create_rectangle(
    143.0,
    564.0,
    1302.0,
    868.0,
    fill="#D8C09B",
    outline="")

canvas.create_rectangle(
    142.0,
    534.0,
    341.0,
    564.0,
    fill="#A73E3E",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    57.0,
    900.0,
    fill="#D8C09B",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    57.0,
    73.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    219.5,
    33.5,
    image=entry_image_1
)
entry_total_bp = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_total_bp.place(
    x=142.0,
    y=23.0,
    width=155.0,
    height=19.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    721.5,
    342.5,
    image=entry_image_2
)
entry_library_contents = Text(
    bd=0,
    bg="#D8C09B",
    highlightthickness=0,
	font=("Goudy Old Style",10,"bold")
)
entry_library_contents.place(
    x=142.0,
    y=166.0,
    width=1159.0,
    height=351.0
)

canvas.create_text(
    142.0,
    0.0,
    anchor="nw",
    text="Library Build Points:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

#entry_image_3 = PhotoImage(
#    file=relative_to_assets("entry_3.png"))
#entry_bg_3 = canvas.create_image(
#    815.0,
#    611.0,
#    image=entry_image_3
#)

entry_scriptorium_title = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_title.place(
    x=640.0,
    y=593.0,
    width=622.0,
    height=34.0
)

canvas.create_text(
    640.0,
    570.0,
    anchor="nw",
    text="Book Title",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

canvas.create_text(
    164.0,
    571.0,
    anchor="nw",
    text="Select Book",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    720.0,
    783.0,
    image=entry_image_4
)
entry_scriptorium_description = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_description.place(
    x=164.0,
    y=723.0,
    width=1112.0,
    height=118.0
)

canvas.create_text(
    164.0,
    703.0,
    anchor="nw",
    text="Description",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    219.5,
    81.5,
    image=entry_image_5
)
entry_unused_bp = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_unused_bp.place(
    x=142.0,
    y=71.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    142.0,
    48.0,
    anchor="nw",
    text="Unused Build Points:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    409.5,
    33.5,
    image=entry_image_6
)
entry_tractatus_min_quality = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_tractatus_min_quality.place(
    x=332.0,
    y=23.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    332.0,
    0.0,
    anchor="nw",
    text="Tractatus Min Quality:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    580.5,
    33.5,
    image=entry_image_7
)
entry_tractatus_max_quality = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_tractatus_max_quality.place(
    x=503.0,
    y=23.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    503.0,
    0.0,
    anchor="nw",
    text="Tractatus Max Quality:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    580.5,
    81.0,
    image=entry_image_8
)
entry_summa_max_level = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_summa_max_level.place(
    x=503.0,
    y=70.0,
    width=155.0,
    height=20.0
)

canvas.create_text(
    503.0,
    48.0,
    anchor="nw",
    text="Summa Max Level:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    409.5,
    81.0,
    image=entry_image_9
)
entry_summa_min_level = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_summa_min_level.place(
    x=332.0,
    y=70.0,
    width=155.0,
    height=20.0
)

canvas.create_text(
    332.0,
    48.0,
    anchor="nw",
    text="Summa Min Level:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    580.5,
    127.0,
    image=entry_image_10
)
entry_summa_max_quality = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_summa_max_quality.place(
    x=503.0,
    y=116.0,
    width=155.0,
    height=20.0
)

canvas.create_text(
    503.0,
    94.0,
    anchor="nw",
    text="Summa Max Quality:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

canvas.create_text(
    673.0,
    94.0,
    anchor="nw",
    text="Favoured Topics:",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_favoured_topics = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
	font=("Goudy Old Style",10,"bold")
)
entry_favoured_topics.place(
    x=673.0,
    y=116.0,
    width=559.0,
    height=40.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    409.5,
    127.0,
    image=entry_image_11
)
entry_summa_min_quality = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_summa_min_quality.place(
    x=332.0,
    y=116.0,
    width=155.0,
    height=20.0
)

canvas.create_text(
    332.0,
    94.0,
    anchor="nw",
    text="Summa Min Quality",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

canvas.create_text(
    161.0,
    142.0,
    anchor="nw",
    text="Library Contents",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_generate = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=bookgen,
    relief="flat"
)
button_generate.place(
    x=710.0,
    y=44.0,
    width=163.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_save = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=savelib,
    relief="flat"
)
button_save.place(
    x=914.0,
    y=44.0,
    width=163.0,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_load = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=loadlib,
    relief="flat"
)
button_load.place(
    x=1118.0,
    y=44.0,
    width=163.0,
    height=39.0
)

canvas.create_text(
    154.0,
    540.0,
    anchor="nw",
    text="Scriptorium (Book Editor)",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    608.5,
    682.5,
    image=entry_image_12
)
entry_scriptorium_subject = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_subject.place(
    x=531.0,
    y=672.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    531.0,
    650.0,
    anchor="nw",
    text="Subject",
    fill="#FFFFFF",
    #font=("Goudy Old Style",12,"bold")
	font=("Goudy Old Style",12,"bold")
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    431.5,
    682.5,
    image=entry_image_13
)
entry_scriptorium_type = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_type.place(
    x=354.0,
    y=672.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    354.0,
    650.0,
    anchor="nw",
    text="Type",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    785.5,
    682.5,
    image=entry_image_14
)
entry_scriptorium_language = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_language.place(
    x=708.0,
    y=672.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    708.0,
    650.0,
    anchor="nw",
    text="Language",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    962.5,
    682.5,
    image=entry_image_15
)
entry_scriptorium_quality = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_quality.place(
    x=885.0,
    y=672.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    888.0,
    650.0,
    anchor="nw",
    text="Quality",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    1139.5,
    682.5,
    image=entry_image_16
)
entry_scriptorium_level = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_scriptorium_level.place(
    x=1062.0,
    y=672.0,
    width=155.0,
    height=19.0
)

canvas.create_text(
    1065.0,
    650.0,
    anchor="nw",
    text="Level",
    fill="#FFFFFF",
    font=("Goudy Old Style",12,"bold")
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_scriptorium_save = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=savebook,
    relief="flat"
)
button_scriptorium_save.place(
    x=164.0,
    y=671.0,
    width=101.0,
    height=22.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_scriptorium_delete = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_scriptorium_delete.place(
    x=276.0,
    y=671.0,
    width=59.0,
    height=22.0
)

book_name_list = ["Create New"]
book_list_var = tk.StringVar()
book_list_var.set(book_name_list[0]) # default value

#book_list_select = OptionMenu(window,book_list_var,test_list[0],*test_list)
book_list_select = ttk.Combobox(window,textvariable=book_list_var,values=book_name_list)
book_list_select.bind('<<ComboboxSelected>>', populate_scriptorium)   

book_list_select.place(
    x=160.0,
    y=600.0,
    width=450.0,
    height=25.0
)

entry_total_bp.insert("end","0")
entry_total_bp.config(state= "disabled")
entry_summa_max_level.insert("end","8/20")
entry_summa_max_level.config(state= "disabled")
entry_summa_min_level.insert("end","1/1")
entry_summa_min_level.config(state= "disabled")
entry_summa_max_quality.insert("end","22")
entry_summa_max_quality.config(state= "disabled")
entry_summa_min_quality.insert("end","1")
entry_tractatus_max_quality.insert("end","11")
entry_tractatus_min_quality.insert("end","1")
entry_unused_bp.insert("end","0")
entry_scriptorium_quality.insert("end","0")
entry_scriptorium_level.insert("end","0")
entry_scriptorium_language.insert("end","Latin")
entry_scriptorium_type.insert("end","Tractatus")
entry_scriptorium_subject.insert("end","None")

window.resizable(False, False)
window.mainloop()
