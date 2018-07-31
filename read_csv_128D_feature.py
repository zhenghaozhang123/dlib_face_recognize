import cv2
import os
import dlib
from skimage import io
import csv
import numpy as np
import pandas as pd

path_pics = "D:/yoorstore/face_recognize1/get_from_camera/"
path_csv = "D:/yoorstore/face_recognize1/csvs/"

# detector to find the faces
detector = dlib.get_frontal_face_detector()

# shape predictor to find the face landmarks
predictor = dlib.shape_predictor("D:/yoorstore/face_recognize1/shape_predictor_68_face_landmarks.dat")

# face recognition model, the object maps human faces into 128D vectors
facerec = dlib.face_recognition_model_v1("D:/yoorstore/face_recognize1/dlib_face_recognition_resnet_model_v1.dat")


# ���ص���ͼ���128D����
def return_128d_features(path_img):
    img = io.imread(path_img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(img_gray, 1)

    print("��������ͼ��", path_img, "\n")

    # ��Ϊ�п��ܽ�������������ȥ��⣬��ⲻ����������
    # ����Ҫȷ���� ��⵽����������ͼ�� ��ȥ������
    if len(dets) != 0:
        shape = predictor(img_gray, dets[0])
        face_descriptor = facerec.compute_face_descriptor(img_gray, shape)
    else:
        face_descriptor = 0
        print("no face")

    # print(face_descriptor)
    return face_descriptor


# return_128d_features(path_pics+"img_face_13.jpg")

# ���ļ�������Ƭ������ȡ������д��csv
# ����input:
#   path_pics:  ͼ���ļ��е�·��
#   path_csv:   Ҫ���ɵ�csv·��

def write_into_csv(path_pics, path_csv):
    dir_pics = os.listdir(path_pics)

    with open(path_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(dir_pics)):
            # ����return_128d_features()�õ�128d����
            print("���ڶ�������ͼ��", path_pics + dir_pics[i])
            features_128d = return_128d_features(path_pics + dir_pics[i])
            #  print(features_128d)
            # ����û�м���������ͼƬ����
            if features_128d == 0:
                i += 1
            else:
                writer.writerow(features_128d)


write_into_csv(path_pics, path_csv + "default_person.csv")

path_csv_rd = "D:/yoorstore/face_recognize1/csvs/default_person.csv"


# ��csv�ж�ȡ���ݣ�����128d�����ľ�ֵ
feature_mean=[]
def compute_the_mean(path_csv_rd):
    column_names = []

    # 128������
    for i in range(128):
        column_names.append("features_" + str(i + 1))

    # ����pandas��ȡcsv
    rd = pd.read_csv(path_csv_rd, names=column_names)

    # ���128ά�����ľ�ֵ
    

    for i in range(128):
        tmp_arr = rd["features_" + str(i + 1)]
        tmp_arr = np.array(tmp_arr)

        # ����ĳһ�������ľ�ֵ
        tmp_mean = np.mean(tmp_arr)

        feature_mean.append(tmp_mean)

    print(feature_mean)
    return feature_mean

# compute_the_mean(path_csv_rd)
