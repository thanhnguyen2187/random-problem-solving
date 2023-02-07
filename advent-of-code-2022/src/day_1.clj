(ns day-1
  (:require [clojure.string :as str]))

(defn to-ints
  [seq]
  (map #(Integer/parseInt %) seq))

(defn sum
  [seq]
  (reduce + seq))

;; part 1
(as-> (slurp "inputs/day_1.txt") _
      (str/split _ #"\n\n")
      (map str/trim-newline _)
      (map #(str/split % #"\n") _)
      (map to-ints _)
      (map sum _)
      (sort > _)
      (first _))

;; part 2
(as-> (slurp "inputs/day_1.txt") _
      (str/split _ #"\n\n")
      (map str/trim-newline _)
      (map #(str/split % #"\n") _)
      (map to-ints _)
      (map sum _)
      (sort > _)
      (take 3 _)
      (sum _))
