import decipher
import freqanalysis

freqanalysis.generate_table('file_to_be_decoded.txt', 'frequency_table.txt')

decipher.decipher('file_to_be_decoded.txt', 'decoded_file.txt')
