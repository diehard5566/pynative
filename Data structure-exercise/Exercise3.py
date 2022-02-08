# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = sample_list[:3]
re_chunk1 = chunk1[::-1]

chunk2 = sample_list[3:6]
re_chunk2 = chunk2[::-1]

chunk3 = sample_list[6:]
re_chunk3 = chunk3[::-1]

print("Chunk 1", chunk1)
print("After reversing it", re_chunk1)

print("Chunk 2", chunk2)
print("After reversing it", re_chunk2)

print("Chunk 3", chunk3)
print("After reversing it", re_chunk3)
