import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*
fun main(args: Array<String>)
{
 val input=Scanner(System.`in`)
 var userInput=input.nextInt()
 var modulus: Int;
 modulus=userInput%2;
 if(userInput>=1&&userInput<=100)
 {
     if(modulus==1)
     {
       print("Weird")
     }
     else if(userInput>=2&&userInput<=5)
     {
       print("Not Weird")
       
     }
     else if(userInput>=6&&userInput<=20)
     {
       print("Weird")
     }
     else 
     {
         print("Not Weird")
     }
 }
}
