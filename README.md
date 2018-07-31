# dlib_face_recognize
-------让系统认识我-------

-------人脸识别系统-------

---VERSION1：基于DLIB实现人脸识别

---缺点： 

1.判定是否同一个人的阈值难以确定。

2.模型适合小型人脸数据库，一旦人脸数据库人数过多，此处的阈值更加难以确定

3.同时，一旦数据库新的人员进入，需要重新调整阈值，不符合实际产品落实

---优点：

方便简单，可以用来实现小型数据库样本的识别。比如：想要通过电脑摄像头来实现人脸开机，只需要将单独个人的人脸录入单个人脸数据库。


此处为版本1.通过DLIB，向量间欧式距离，来实现人脸识别系统。

文件解析：

get_from_camera.py  -----通过电脑摄像头实现对自己人脸的抓取，并储存在个人人脸数据库中，以备后面进行识别。

read_csv_128D_feature.py 

1.对摄像头抓拍下来的自己的人脸数据库进行特征转换，将自己的每一张人脸照片转换为128D特征;

2.计算完每一张人脸照片128D值后，进行取平均值。取平均值的目的在于：将所有的照片进行一次平均，行成平均脸。可以排除部分照片将自己的人脸某部分特征放大/放小。好比，如果将10岁的你的照片和30岁的你的照片单独分开进行对照。就很难区分是否是本人，但是如果将两张照片进行一次平均，形成此人地平均脸（10岁的你特征占一部分，30岁的你特征占一部分），就可以更为清晰地认出是本人。
			 
			
			 
recognize_sb.py     -----完成上面两步骤后，就可以通过电脑摄像头的拍摄，来判定是不是本人。此处的dist就是阈值。

shape_predictor_5_face_landmarks.dat  -----人脸鉴别基于5个特征点。（https://download.csdn.net/download/u010039305/10413357?utm_source=bbsseo 为下载地址）

shape_predictor_68_face_landmarks.dat -----人脸鉴别基于68个特征点（https://download.csdn.net/download/baiyu_king/10427803 为下载地址）

dlib_face_recognition_resnet_model_v1 -----人脸128D特征转换包 （建议如果想让模型更加准确，自己进行人脸特征转换，最常见为通过卷积神经网络来实现特征取值，后续会讲）（https://download.csdn.net/download/googler_offer/10190598  为下载地址）


阈值的确定：

1.对于单样本数据库，可以通过给dist设定一个范围，来查看精确度。来选定dist值。（需要用多张照片进行比对得出此值）

2.之所以说此模型只适合于单样本数据库，因为一旦我们的数据库录入多人系统， 我们设定的dist值就会大波动，而不是小范围变动。好比A同学的最佳dist值在0.4，B同学的最佳dist值在0.7.然后我们会进行取平均值5.5。此处的5.5明显是合适的，会让结果非常的不准确。所以此模型不适用于多样本数据库。
			
备注：这个模型是做系统识别时候的个人见解，如果存在知识点上的误导，希望大家可以email来联系我：493200517@qq.com
