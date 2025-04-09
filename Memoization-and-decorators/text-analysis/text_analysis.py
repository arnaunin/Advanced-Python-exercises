import functools
import re
import time

@functools.lru_cache(maxsize=None)
def calculate_word_frequency(text):
    # Text preprocessing
    text = text.lower()
    text = re.sub(r'[^a-záéíóúüñ\s]', '', text)  # Remove punctuation and unwanted characters
    words = text.split()
    
    # Exclude common words
    common_words = set(["el", "la", "los", "las", "de", "en", "y", "a", "con", "es", "un", "una", "para"])
    
    words = [word for word in words if word not in common_words]
    
    # Frequency counting
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Usage example
text_1 = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
adarga antigua, rocín flaco y galgo corredor.
Una olla de algo más vaca que carnero, salpicón las más noches,
duelos y quebrantos los sábados, lentejas los viernes,
algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.
El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo,
los días de entre semana se honraba con su vellorí de lo más fino.
Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte,
y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera.
Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes,
enjuto de rostro, gran madrugador y amigo de la caza.
Quieren decir que tenía el sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia en los autores que deste caso escriben),
aunque por conjeturas verosímiles se deja entender que se llama Quijana;
pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.
"""

text_2 = "Otro ejemplo de Análisis de texto con palabras repetidas. Ejemplo y texto se repiten."

start_1 = time.time()
frequency_without_memo_1 = calculate_word_frequency(text_1)
frequency_without_memo_2 = calculate_word_frequency(text_2)
end_1 = time.time()

start_2 = time.time()
frequency_with_memo_1 = calculate_word_frequency(text_1)
frequency_with_memo_2 = calculate_word_frequency(text_2)
end_2 = time.time()

print("Word frequency for text_1 without memoization: ", frequency_without_memo_1)
print("Word frequency for text_2 without memoization: ", frequency_without_memo_2)
print("Word frequency for text_1 with memoization: ", frequency_with_memo_1)
print("Word frequency for text_2 with memoization: ", frequency_with_memo_2)

print("Time without memoization: ", (end_1 - start_1))
print("Time with memoization: ", (end_2 - start_2))