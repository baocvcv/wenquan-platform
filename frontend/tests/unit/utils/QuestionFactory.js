class QuestionFactory {
    constructor() {}
    create_single_choice(id) {
        return {
            "id": id,
            "parents_node": [0],
            "history_version_id":1,
            "question_change_time": "2019-10-15T01:11:21.754312Z",
            "question_name": "question1",
            "question_type": "single",
            "question_level": 5,
            "question_content": "人类的本质是?",
            "question_image": [""],
            "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"],
            "question_ans": "D",
            "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
        }
    }
}

export default QuestionFactory;