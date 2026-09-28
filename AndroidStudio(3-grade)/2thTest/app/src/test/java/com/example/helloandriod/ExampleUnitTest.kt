package com.example.helloandriod

import android.util.Log
import org.junit.Test
import org.junit.Assert.*

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class ExampleUnitTest {
    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)

        // 가변 변수(var)와 불변 변수(val)
        var myAge = 20 // Int형 자동 추론 (값 변경 가능)
        myAge = 25 // 값 재할당 가능
        val myName = "홍길동" // String형 자동 추론 (읽기 전용, 재할당 불가)
        val age: Int = 25 // 명시적 Int형 지정
 // 기본 자료형 (Primitive Types)
        val numInt: Int = 20 // 정수형 (Int, Long, Byte, Short)
        val numLong: Long = 3000000000L // Long형 식별자 L
        val numDouble: Double = 3.14159 // 실수형 (Double, Float)
        val numFloat: Float = 3.14f // Float형 식별자 f
        val isBoolean: Boolean = true // 논리형 (Boolean)
        val letter: Char = 'A' // 문자형 (Char)
        val text: String = "Hello" // 문자열 (String)
        var a: Int = 10
        var b: Int = 3
        val sum = a + b // 더하기 (13)
        val mod = a % b // 나머지 (1)

        //a++ // 증감 연산자 (11)
        val isEqual = (a == b) // 비교 연산자 (false)
        val isGreater = (a > b) // 비교 연산자 (true)
        val isTrue = (a > 0) && (b > 0) // 논리 연산자 AND (true)
        var myArray: IntArray = intArrayOf(1,2,3,4,5)

        var myX: Int = 100
        var myY: Float = myX.toFloat()

        println("코틀린 : 산술연산자, a+b :" + (a+b))
        println("코틀린 : 산술연산자, a-b :" + (a-b))
        println("코틀린 : 산술연산자, a/b :" + (a/b))
        println("코틀린 : 산술연산자, a*b :" + (a*b))

        println("코틀린 : 자료형변환, Int : $myX")
        println("코틀린 : 자료형변환, Float : $myY")
        println("배열자료형 Arrlay = ${myArray[2]}")
        println("코틀린 : 정수 자료형, Int : $numInt")
        println("코틀린 : 정수 자료형, numLong : $numLong")
        println("코틀린 : 정수 자료형, numDouble : $numDouble")
        println("코틀린 : 정수 자료형, numFloat : $numFloat")
        println("코틀린 : 정수 자료형, isBoolean : $isBoolean")
        println("코틀린 : 정수 자료형, letter : $letter")
        println("코틀린 : 정수 자료형, text :  $text")

        println("코틀린 : 정수 자료형, sum : $sum")
        println("코틀린 : 정수 자료형, mod : $mod")
        println("코틀린 : 정수 자료형, isEqual : $isEqual")
        println("코틀린 : 정수 자료형, isGreater : $isGreater")
        println("코틀린 : 정수 자료형, isTrue : $isTrue")
// 1) if ~ else if ~ else 문
        var num: Int = -10
        var result: String
        if (num > 0) {
            result = "양수"
        } else if (num == 0) {
            result = "0"
        } else {
            result = "음수"
        }
        println("코틀린 :  if ~ else if ~ else 문 : $result")


// 표현식(Expression)으로 직접 값 할당
        num = 101
        val status = if (num > 0) "양수" else "음수 또는 0"
      //  val input = readln()
      //  val num1 = input.toIntOrNull() ?: 0 // 숫자가 아니면 기본값 0 대입
// 2) 중첩 if 문
        if (num > 0) {
            if (num % 2 == 0) result = "양수 및 짝수" else result = "양수 및 홀수"
        } else {
            if (num % 2 == 0) result = "음수 및 짝수" else result = "음수 및 홀수"
        }
        println("코틀린 :  표현식(Expression)으로 직접 값 할당 : $result")

// 3) when 문 (switch 대체)
        var day: Int = 5
        var dayName = when (day) {
            1 -> "Monday"
            2 -> "Tuesday"
            3 -> "Wednesday"
            4 -> "Thursday"
            5 -> "Friday"
            6, 7 -> "Weekend" // 여러 값 결합
            in 8..10 -> "Special" // 범위(in 연산자) 검사
            else -> "Invalid day" // 기본값
        }

        println("코틀린 :  when 문 (switch 대체) : $dayName")

        // 1) for 문 - 범위 및 역순 순회
        for (i in 1..5) { // 1부터 5까지 순차 증가 (1, 2, 3, 4, 5)
            println("for i : $i")

        }
        for (i in 10 downTo 1) { // 5부터 1까지 역순 감소 (5, 4, 3, 2, 1)
            println("for i : $i")
        }
        for (i in 20 downTo 1 step 2) {// 2씩 감소하며 역순 순회 (5, 3, 1)
            println("for i : $i")
        }

        // 2) 배열 요소 및 인덱스 반복
        var numbers = arrayOf(1, 2, 3, 4, 5)
        for (num in numbers) { // 요소 직접 순회
            if (num % 2 == 0) println("for 홀수: $num")
        }
        for (i in numbers.indices) { // 인덱스(indices) 기반 순회 (0..4)
            println("for i : $i,  ${numbers[i]}")
            //Log.d("for", "index $i = ${numbers[i]}")
        }



    }
}