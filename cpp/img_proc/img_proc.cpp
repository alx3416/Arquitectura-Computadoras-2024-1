#include "img_proc.hpp"

int main(int, char**)
{
    cv::Mat frame, frame_gray, frame_gray_processed;
    cv::Mat image = cv::imread("baboon.png");
    if (image.empty())
    {
        std::cerr << "Failed to load image!" << std::endl;
        return -1;
    }

    cv::cvtColor(image, frame_gray, cv::COLOR_BGR2GRAY);
    frame_gray_processed = frame_gray.clone();
    cv::Mat imagen_double;
    frame_gray.convertTo(imagen_double, CV_64F);
    Eigen::MatrixXd eigen_image = EigenCV::cvMatToEigen(imagen_double / 255);
    // TODO convolution
    Eigen::MatrixXd kernel(3, 3);
    kernel(0, 0) = -1;
    kernel(0, 1) = 0;
    kernel(0, 2) = 1;
    kernel(1, 0) = -2;
    kernel(1, 1) = 0;
    kernel(1, 2) = 2;
    kernel(2, 0) = -1;
    kernel(2, 1) = 0;
    kernel(2, 2) = 1;

    Eigen::MatrixXd eigen_result = EigenCV::eigen_convolution(eigen_image, kernel);

    frame_gray_processed = EigenCV::eigenTocvMat(eigen_result);
    cv::imshow("Image_gray", frame_gray);
    cv::imshow("Image_processed", frame_gray_processed);
    cv::waitKey(0); // Wait for a key press
    return 0;
}