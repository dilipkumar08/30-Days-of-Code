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
fun main()
{
val input=Scanner(System.`in`)
var mealCost=input.nextDouble()
var tax=input.nextDouble()
var tips=input.nextDouble()
tax=(tax*mealCost)/100;
tips=(tips*mealCost)/100;
val total=(tax+tips+mealCost)
roundtonearest(total)
}
fun roundtonearest(totalCost: Double)
{
    val a: Int;
    a=(totalCost+0.5).toInt()
    println(a)
}
