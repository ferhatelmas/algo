package arrays_and_sorting.tutorial_intro

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val l = Source.stdin.getLines
    val v = l.next
    println(l.drop(1).next.split("\\s").zipWithIndex.find(_._1 == v) match {
      case Some((_, i)) => i
    })
  }
}
