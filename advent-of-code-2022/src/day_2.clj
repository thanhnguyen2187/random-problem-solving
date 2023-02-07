(ns day-2
  (:require [clojure.core.match :refer [match]]
            [clojure.string :as str]))

(def character-to-shape
  {"A" :Rock
   "B" :Paper
   "C" :Scissors
   "X" :Rock
   "Y" :Paper
   "Z" :Scissors})

(def character-to-outcome
  {"X" :lose
   "Y" :draw
   "Z" :win})

(def shape-to-score
  {:Rock 1
   :Paper 2
   :Scissors 3})

(def outcome-to-score
  {:win 6
   :draw 3
   :lose 0})

(defn pick-opponent-shape
  [shape outcome]
  (match
    [shape outcome]
    [_ :draw] shape
    [:Rock     :win] :Paper
    [:Paper    :win] :Scissors
    [:Scissors :win] :Rock
    [:Rock     :lose]  :Scissors
    [:Paper    :lose]  :Rock
    [:Scissors :lose]  :Paper
    :else (throw (ex-info "day-2.pick-opponent-shape unreachable path"
                          {:shape shape
                           :outcome outcome}))))

(defn lesser
  [shape-1 shape-2]
  (match
    [shape-1 shape-2]
    [:Rock     :Paper]    true
    [:Paper    :Scissors] true
    [:Scissors :Rock]     true
    [:Rock     (:or :Rock :Scissors)] false
    [:Paper    (:or :Rock :Paper)] false
    [:Scissors (:or :Paper :Scissors)] false
    :else (throw (ex-info "day-2.lesser unreachable path"
                          {:shape-1 shape-1
                           :shape-2 shape-2}))
    ))

(defn outcome
  [shape-1 shape-2]
  (cond
    (= shape-1 shape-2) [:draw :draw]
    (lesser shape-1 shape-2) [:lose :win]
    (lesser shape-2 shape-1) [:win :lose]
    :else (throw (ex-info "day-2.outcome unreachable path"
                          {:shape-1 shape-1
                           :shape-2 shape-2}))
    ))

;; part 1
(as-> (slurp "inputs/day_2.txt") _
      (str/split-lines _)
      (map (fn [pair] (str/split pair #" ")) _)
      (map (fn [[character-1 character-2]]
             [(get character-to-shape character-1)
              (get character-to-shape character-2)])
           _)
      (map (fn [[shape-1 shape-2]]
             (let [[outcome-1 outcome-2] (outcome shape-1 shape-2)]
               (+ (get shape-to-score shape-2)
                  (get outcome-to-score outcome-2))))
           _)
      (reduce + _))

;; part 2
(as-> (slurp "inputs/day_2.txt") _
      (str/split-lines _)
      (map (fn [pair] (str/split pair #" ")) _)
      (map (fn [[character-1 character-2]]
             [(get character-to-shape character-1)
              (get character-to-outcome character-2)])
           _)
      (map (fn [[shape outcome]]
             (let [opponent-shape (pick-opponent-shape shape outcome)]
               (+ (get shape-to-score opponent-shape)
                  (get outcome-to-score outcome))))
           _)
      (reduce + _))
