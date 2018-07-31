import dlib         # ����ʶ��Ŀ�dlib
import numpy as np  # ���ݴ���Ŀ�numpy
import cv2          # ͼ����Ŀ�OpenCv

# dlibԤ����
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('D:/yoorstore/face_recognize1/shape_predictor_68_face_landmarks.dat')

# ����cv2����ͷ����
cap = cv2.VideoCapture(0)

# cap.set(propId, value)
# ������Ƶ������propId���õ���Ƶ������value���õĲ���ֵ
cap.set(3, 480)

# ��ͼscreenshoot�ļ�����
cnt_ss = 0

# ������ͼ�ļ�����
cnt_p = 0

# ����
path_save = "F:/code/python/P_dlib_face_reco/data/get_from_camera/"

# cap.isOpened���� ����true/false ����ʼ���Ƿ�ɹ�
while cap.isOpened():

    # cap.read()
    # ��������ֵ��
    #    һ������ֵtrue/false�������ж϶�ȡ��Ƶ�Ƿ�ɹ�/�Ƿ���Ƶĩβ
    #    ͼ�����ͼ�����ά����q
    flag, im_rd = cap.read()

    # ÿ֡������ʱ1ms����ʱΪ0��ȡ���Ǿ�̬֡
    kk = cv2.waitKey(1)

    # ȡ�Ҷ�
    img_gray = cv2.cvtColor(im_rd, cv2.COLOR_RGB2GRAY)

    # ������rects
    rects = detector(img_gray, 0)

    # print(len(rects))

    # ����Ҫд������
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(rects) != 0:
        # ��⵽����

        # ���ο�
        for k, d in enumerate(rects):

            # ������δ�С
            # (x,y), (���width, �߶�height)
            pos_start = tuple([d.left(), d.top()])
            pos_end = tuple([d.right(), d.bottom()])

            # ������ο��С
            height = d.bottom() - d.top()
            width = d.right() - d.left()

            # ����������С���ɿյ�ͼ��
            cv2.rectangle(im_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 2)
            im_blank = np.zeros((height, width, 3), np.uint8)
            
            # ����'s'��������ͷ�е�����������
            if kk == ord('s'):
                cnt_p += 1
                for ii in range(height):
                    for jj in range(width):
                        im_blank[ii][jj] = im_rd[d.top() + ii][d.left() + jj]
                # �洢����ͼ���ļ�
                cv2.imwrite(path_save + "img_face_" + str(cnt_p) + ".jpg", im_blank)
                print("д�뱾�أ�", path_save + "img_face_" + str(cnt_p) + ".jpg")

        # ��ʾ������
        cv2.putText(im_rd, "faces: " + str(len(rects)), (20, 50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

    else:
        # û�м�⵽����
        cv2.putText(im_rd, "no face", (20, 50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

    # ���˵��
    im_rd = cv2.putText(im_rd, "s: save face", (20, 400), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    im_rd = cv2.putText(im_rd, "q: quit", (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

    # ����q���˳�
    if kk == ord('q'):
        break

    # ������ʾ
    # cv2.namedWindow("camera", 0) # �����Ҫ����ͷ���ڴ�С�ɵ�
    cv2.imshow("camera", im_rd)

# �ͷ�����ͷ
cap.release()

# ɾ�������Ĵ���
cv2.destroyAllWindows()