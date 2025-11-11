#ifndef ALTO_RENDIMIENTO_IMG_PROC_HPP
#define ALTO_RENDIMIENTO_IMG_PROC_HPP

#include <Eigen/Dense>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include <opencv2/opencv.hpp>
#include <opencv2/core/eigen.hpp>
#include <iostream>
#include <cmath>
#include <omp.h>

namespace EigenCV {
    Eigen::MatrixXd cvMatToEigen(const cv::Mat &mat) {
        Eigen::MatrixXd eigen_mat(mat.rows, mat.cols);
        cv::cv2eigen(mat, eigen_mat);
        return eigen_mat;
    }

    Eigen::MatrixXd eigen_convolution(const Eigen::MatrixXd &image, const Eigen::MatrixXd &kernel) {
        Eigen::MatrixXd res(image.rows(), image.cols());
        res.setZero(); // Initialize to zero
        // TODO Convolution code

        return res;
    }

    cv::Mat eigenTocvMat(const Eigen::MatrixXd &eigen_data) {
        cv::Mat result(eigen_data.rows(), eigen_data.cols(), CV_8U);
        eigen_data.cwiseAbs() * 255;
        cv::eigen2cv(eigen_data, result);
        return result;
    }

}

#endif //ALTO_RENDIMIENTO_IMG_PROC_HPP
