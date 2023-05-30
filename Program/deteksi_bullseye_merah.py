import sys
import cv2 as cv
import numpy as np

def main(argv):
    default_file = 'real_4crop.jpeg'
    filename = argv[0] if len(argv) > 0 else default_file
    src = cv.imread((filename), cv.IMREAD_COLOR)
    if src is None:
        print('Error opening image!')
        return -1
    tinggi, panjang, channels = src.shape
    x_tengah = int(panjang/2)
    y_tengah = int(tinggi/2)
    print(x_tengah, y_tengah)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 1)
    cv.imshow("coba blur", gray)
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.25, rows / 16,
                              param1=110, param2=75,
                              minRadius=50, maxRadius=150)
    x2 = 0
    y2 = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            x2, y2 = (center[0], center[1])
            print(x2, y2)
            cv.circle(src, center, 1, (50, 205, 50), 8)
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 2)
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])

#---------------------- batas

# import sys
# import cv2 as cv
# import numpy as np

# def hitung_max_error(radius_deteksi):
#     radius_max = 307
#     hasil_radius = (radius_deteksi / radius_max) * 100
#     return hasil_radius

# def hitung_akurasi(x1, y1, x2, y2):
#     hasil = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#     akurasi = 100 - hasil
#     print("Akurasi: ", akurasi, "%")
#     return akurasi

# def main(argv):

#     default_file = 'real_1.jpeg'
#     filename = argv[0] if len(argv) > 0 else default_file
#     src = cv.imread((filename), cv.IMREAD_COLOR)
#     if src is None:
#         print('Error opening image!')
#         return -1
#     tinggi, panjang, channels = src.shape
#     x_tengah = int(panjang/2)
#     y_tengah = int(tinggi/2)
#     print(x_tengah, y_tengah)
#     gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
#     gray = cv.medianBlur(gray, 11)
#     cv.imshow("coba blur", gray)
#     rows = gray.shape[0]
#     circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
#                               param1=100, param2=30,
#                               minRadius=50, maxRadius=200)
#     x2 = 0
#     y2 = 0
#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         for i in circles[0, :]:
#             print("cuy")
#             center = (i[0], i[1])
#             x2, y2 = (center[0], center[1])
#             print(x2, y2)
#             cv.circle(src, center, 1, (50, 205, 50), 8)
#             radius = i[2]
#             cv.circle(src, center, radius, (255, 0, 255), 2)
#     akurasi = hitung_akurasi(x_tengah, y_tengah, x2, y2)
#     max_error = hitung_max_error(radius)
#     cv.putText(src, 'Akurasi: {:.2f}%'.format(akurasi), (25, 25), cv.FONT_HERSHEY_SIMPLEX,
#            0.75, (0, 255, 0), 2, cv.LINE_AA)
#     cv.putText(src, 'Max Error: {:.2f}%'.format(max_error), (25, 50), cv.FONT_HERSHEY_SIMPLEX,
#            0.75, (0, 255, 0), 2, cv.LINE_AA)
#     cv.imshow("detected circles", src)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


# if __name__ == "__main__":
#     main(sys.argv[1:])


