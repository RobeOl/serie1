from music21 import *
from multidimensional import genera_multidimensional


def genera_sequenza(seq_type, tipo, note_len,
                    i, j,
                    i1, j1, i2, j2,
                    ii1, jj1, ii2, jj2, ii3, jj3,
                    int_i, int_j, int_k,
                    ottave, bass_clef, starting_note, harmony, harmony_type,
                    multi_values=None):
    # Rimasto da GeCo-Tool
    # Dispatcher verso il generatore corretto in base a seq_type.

    # Parametri aggiuntivi rispetto alla versione precedente
    # -------------------------------------------------------
    # multi_values : list[int] | None
    #     Lista di K interi (intervalli in semitoni) per la modalità
    #     Multidimensional.  Se None o lista vuota viene usata [0].
  
    # elif seq_type == "Multidimensional":
    n_K = multi_values if multi_values else [0]
    s = genera_multidimensional(tipo, note_len, n_K,
                                ottave, bass_clef, starting_note, harmony, harmony_type)

    return s
