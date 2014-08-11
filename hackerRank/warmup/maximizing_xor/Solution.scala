package warmup.maximizing_xor

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val r = Source.stdin.bufferedReader
    val (a, b) = (r.readLine.toInt, r.readLine.toInt)
    val it = for(i <- a until b; j <- (a+1) to b) yield i ^ j
    println(if(it.nonEmpty) it.max else 0)
  }
}
