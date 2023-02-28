(ns day-6
  (:require [clojure.string :as str]))

;; part 1
(->> (slurp "inputs/day_6.txt")
     (str/trim-newline)
     (zipmap (range))
     (into (sorted-map))
     (partition 4 1)
     (filter (fn [pairs]
               (let [characters (vals pairs)]
                 (= (count characters)
                    (count (set characters))))))
     (first)
     (last)
     ((fn [[index character]]
        (inc index))))

;; part 2
(->> (slurp "inputs/day_6.txt")
     (str/trim-newline)
     (zipmap (range))
     (into (sorted-map))
     (partition 14 1)
     (filter (fn [pairs]
               (let [characters (vals pairs)]
                 (= (count characters)
                    (count (set characters))))))
     (first)
     (last)
     ((fn [[index character]]
        (inc index))))
