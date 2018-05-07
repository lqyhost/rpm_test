//
// Created by qianyong liu on 2018/5/8.
//

/*************************************************************************
    > File Name: hello.h
    > Author: ma6174
    > Mail: ma6174@163.com
    > Created Time: Mon 22 Dec 2014 01:09:54 PM HKT
 ************************************************************************/
#ifndef CMAKE_FEI_HELLO_H
#define CMAKE_FEI_HELLO_H
#ifdef _WIN32
#if LIBHELLO_BUILD
        #define LIBHELLO_API __declspec(dllexport)
    #else
        #define LIBHELLO_API __declspec(dllimport)
    #endif
#else
#define LIBHELLO_API
#endif
LIBHELLO_API void hello(const char *name);
//static library is simple as normal c code.
#endif

