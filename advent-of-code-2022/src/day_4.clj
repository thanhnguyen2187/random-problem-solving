(ns day-4
  (:require [clojure.string :as str]))

(defn to-section-assignments
  [text]
  (as-> text _
        (str/split _ #"[-,]")
        (map #(Integer/parseInt %) _)))

(defn assignments-include?
  [[id-1 id-2 id-3 id-4]]
  (or (and (<= id-3 id-1 id-4)
           (<= id-3 id-2 id-4))
      (and (<= id-1 id-3 id-2)
           (<= id-1 id-4 id-2))))

(defn assignments-intersect?
  [[id-1 id-2 id-3 id-4]]
  (or (<= id-3 id-1 id-4)
      (<= id-3 id-2 id-4)
      (<= id-1 id-3 id-2)
      (<= id-1 id-4 id-2)))

(assignments-include? (to-section-assignments "6-54,7-55"))

;; part 1
(->> (slurp "inputs/day_4.txt")
     (str/trim-newline)
     (str/split-lines)
     (map to-section-assignments)
     (map assignments-include?)
     (filter true?)
     (count))

;; part 2
(->> (slurp "inputs/day_4.txt")
     (str/trim-newline)
     (str/split-lines)
     (map to-section-assignments)
     (map assignments-intersect?)
     (filter true?)
     (count))
