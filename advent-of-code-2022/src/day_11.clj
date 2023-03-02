(ns day-11
  (:require [clojure.string :as str]
            [clojure.core.match :refer [match]]
            [instaparse.core :as insta]))

(defn create-monkey
  [operation-line test-lines])

(def sample-monkey
  {:worry-levels  [79 98]
   :operation-fn  (fn [old] (* old 19))
   :test-fn       (fn [value]
                    (if (-> value
                            (mod 19)
                            (= 0))
                      2
                      3))
   :inspect-count 0})

(def parse-monkeys
  (insta/parser
    "monkeys = monkey {<newline> monkey}
     monkey = header starting-items operation test

     id = number
     header = <'Monkey '> id <':'> <newline>
     starting-items = <{blank-space}> <'Starting items: '> number {<', '> number} <newline>
     operation = <{blank-space}> <'Operation: '> operation-text <newline>
     test = condition true-clause false-clause
     condition = <{blank-space}> <'Test: '> condition-text <newline>
     true-clause = <{blank-space}> <'If true: '> clause-text <newline>
     false-clause = <{blank-space}> <'If false: '> clause-text <newline>

     number = #'[0-9]+'
     newline = '\n'
     blank-space = ' '+
     condition-text = #'[0-9a-zA-Z ]+'
     operation-text = #'[0-9a-zA-Z *+=]+'
     clause-text = #'[0-9a-zA-Z ]+'
     "))

(defn parse-operation-text
  [text]
  (let [parts (->> (str/split text #" ")
                   (map str/trim)
                   (filter (fn [part]
                             (not (= part "")))))
        [operand-1 operator-1
         operand-2 operator-2 operand-3] parts]
    (eval `(fn [~'old]
             (~(read-string operator-2)
               ~(read-string operand-2)
               ~(read-string operand-3))))))

(-> (parse-operation-text (identity "new = old + old"))
    (apply [6])
    )

(defn parse-condition-text
  [text]
  (let [parts (str/split text #" ")
        number (-> parts
                   (last)
                   (Integer/parseInt))]
    (fn [x] (-> x
                (mod number)
                (= 0)))))

(defn parse-condition-clause-text
  [text]
  (let [parts (str/split text #" ")
        number (-> parts
                   (last)
                   (Integer/parseInt))]
    number))

(defn parse-monkey-index
  [monkey]
  (->> (get-in monkey [1 1 1 1])
       (Integer/parseInt)))

(defn parse-monkey-items
  [monkey]
  (->> (get monkey 2)
       (drop 1)
       (map (fn [[tag item-str]]
              (Integer/parseInt item-str)))
       (into [])))

(defn parse-monkey-operation-fn
  [monkey]
  (parse-operation-text (get-in monkey [3 1 1])))

(defn parse-monkey-test-fn
  [monkey
   destination-true
   destination-false]
  (let [predicate (->> (get-in monkey [4 1 1 1])
                       (parse-condition-text))
        func (fn [x] (if (predicate x)
                       destination-true
                       destination-false))]
    func))

(defn parse-monkey-test-destination-true
  [monkey]
  (->> (get-in monkey [4 2 1 1])
       (parse-condition-clause-text)))

(defn parse-monkey-test-destination-false
  [monkey]
  (->> (get-in monkey [4 3 1 1])
       (parse-condition-clause-text)))

(defn parse-monkey
  [monkey]
  {:index         (parse-monkey-index monkey)
   :worry-levels  (parse-monkey-items monkey)
   :operation-fn  (parse-monkey-operation-fn monkey)
   :test-fn       (parse-monkey-test-fn
                    monkey
                    (parse-monkey-test-destination-true monkey)
                    (parse-monkey-test-destination-false monkey))
   :inspect-count 0
   })

(parse-monkey
  [:monkey
   [:header [:id [:number "1"]]]
   [:starting-items [:number "54"] [:number "65"] [:number "75"] [:number "74"]]
   [:operation [:operation-text "new = old + 6"]]
   [:test
    [:condition [:condition-text "divisible by 19"]]
    [:true-clause [:clause-text "throw to monkey 2"]]
    [:false-clause [:clause-text "throw to monkey 0"]]]
   ])

(defn advance-turn
  [state index]
  (let [monkey (nth state index)
        worry-levels (monkey :worry-levels)
        operation-fn (monkey :operation-fn)
        test-fn (monkey :test-fn)
        items-with-new-holders (map (fn [worry-level]
                                      (let [new-worry-level (-> worry-level
                                                                (operation-fn)
                                                                (/ 3)
                                                                (int))
                                            new-holder (test-fn new-worry-level)]
                                        [new-worry-level new-holder]))
                                    worry-levels)]
    (-> (reduce (fn [state [item new-holder]]
                  (update-in state [new-holder :worry-levels]
                             conj item))
                state
                items-with-new-holders)
        (update-in [index :inspect-count] + (count worry-levels))
        (assoc-in [index :worry-levels] []))))

(defn advance-turn-2
  [state index]
  (let [monkey (nth state index)
        worry-levels (monkey :worry-levels)
        operation-fn (monkey :operation-fn)
        test-fn (monkey :test-fn)
        items-with-new-holders (map (fn [worry-level]
                                      (let [new-worry-level (-> worry-level
                                                                (operation-fn))
                                            new-holder (test-fn new-worry-level)]
                                        [new-worry-level new-holder]))
                                    worry-levels)]
    (-> (reduce (fn [state [item new-holder]]
                  (update-in state [new-holder :worry-levels]
                             conj item))
                state
                items-with-new-holders)
        (update-in [index :inspect-count] + (count worry-levels))
        (assoc-in [index :worry-levels] []))))

(defn advance-round
  [state]
  (reduce advance-turn
          state
          (range (count state))))

(defn advance-round-2
  [state]
  (reduce advance-turn-2
          state
          (range (count state))))

(let [monkeys (->> ;;(slurp "inputs/day_11.txt")
                   (slurp "inputs/day_11_sample.txt")
                   (parse-monkeys)
                   (drop 1)
                   (mapv parse-monkey)
                   )
      part-1-answer (->> monkeys
                         ((apply comp (repeat 20 advance-round)))
                         (map :inspect-count)
                         (sort)
                         (take-last 2)
                         (apply *))
      part-2-answer (->> monkeys
                         ((apply comp (repeat 20 advance-round-2)))
                         (map :inspect-count)
                         (sort)
                         ;;(take-last 2)
                         ;;(apply *)
                         )
      ]
  [part-1-answer
   ;;part-2-answer
   ])


