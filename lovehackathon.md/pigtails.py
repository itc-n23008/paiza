def Check(MaxLength, MaxSongQuant):
    SongQuant, TotalLength = 0, 0
    for n in range(MaxSongQuant):
        SongLength = int(input())
        TotalLength += SongLength
        if TotalLength > MaxLength:
            return SongQuant
        SongQuant += 1
    return "OK"

MaxLength = int(input()) * 60
MaxSongQuant = int(input())

Answer = Check(MaxLength, MaxSongQuant)
print(Answer)

