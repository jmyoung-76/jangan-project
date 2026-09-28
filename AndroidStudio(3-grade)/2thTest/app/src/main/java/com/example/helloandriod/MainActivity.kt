package com.example.helloandriod

import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    lateinit var button : Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)



        val button = findViewById<Button>(R.id.button)
        button.setOnClickListener {
            Toast.makeText(this, "Test 버튼을 눌렀어요", Toast.LENGTH_SHORT).show()
        }

        }
    }
