import matplotlib.pyplot as plt 

# counting sort ana fonksiyonu
def counting_sort(arr):
    max_val=max(arr) # dizideki en büyük değeri bul
    count=[0]*(max_val + 1) #sayma dizisi

    #her elemanının kaç kes tekrarlandığını say
    for num in arr:
        count[num] += 1

    #sayma dizisini kullanarak sıralı dizi
    sorted_arr=[]
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i]) # her elemanı tekrar sayısı kadar ekle

    return sorted_arr, count #sıralı dizi

#öğrenci notlarını oluştur
grades=[85, 90, 78, 92, 88, 76, 95, 89, 80, 85, 90, 92, 78, 85, 88]

#notları sırala ve sayma dizisini al
sorted_grades, count_grades = counting_sort(grades)

#not dağılımını histogram ile görselleştir. 
plt.bar(range(len(count_grades)), count_grades, color='blue')
plt.xlabel('Notlar')
plt.ylabel('Student Number')
plt.title('Öğrenci not Dağıtımı')
plt.show()
print("Sıralanmış notlar")