package warmup.utopian_tree

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(ln <- Source.stdin.getLines.drop(1)) {
      var h = 1
      for(j<- 0 until ln.toInt) {
        if(j%2 == 0) h *= 2
        else h += 1
      }
      println(h)
    }
  }
}
