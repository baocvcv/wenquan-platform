class QuestionFactory {
  constructor() {}
  create_single_choice(id) {
    return {
      id: id,
      parents_node: [0],
      history_version_id: 1,
      question_change_time: "2019-10-15T01:11:21.754312Z",
      question_name: "question1",
      question_type: "single",
      question_level: 5,
      question_content: "关于人类的本质，下列说法中正确的一项是？",
      question_image: [""],
      question_choice: ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"],
      question_ans: "D",
      question_solution: "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
    };
  }

  create_brief_answer(id) {
    return {
      id: id,
      history_version_id: 11,
      question_name: "quesion5",
      question_type: "brief_ans",
      question_level: 5,
      question_change_time: "2019-10-24T12:20:58.194766Z",
      question_content: "人类的本质是?",
      question_image: ["a"],
      question_ans: "复读机",
      question_solution: "因为人类的本质是复读机",
      parents_node: [2]
    };
  }

  create_question_for_creation() {
    return {
      id: 233,
      history_version_id: 11,
      question_name: "quesion5",
      question_type: "brief_ans",
      question_level: 5,
      question_change_time: "2019-10-24T12:20:58.194766Z",
      question_content: "人类的本质是?",
      question_image: ["a"],
      question_ans: "复读机",
      question_solution: "因为人类的本质是复读机",
      parents_node: []
    };
  }
}

export default QuestionFactory;
