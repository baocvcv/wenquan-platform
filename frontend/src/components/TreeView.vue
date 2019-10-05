<template>
    <div class="tree-view">
        <tree
        :data="treeData"
        :onDrag="onTreeDataChange"
        :fixed="true"
        :height="300"
        :isdraggable="true"></tree>
    </div>
</template>

<script>
import tree from "drag-tree-table"
//https://github.com/mafengwo/vue-drag-tree-table
export default {
    name: "tree-view",
    components: {
        tree
    },
    data: function(){
        return {
            treeData: {
                columns: [
                    {
                        type: 'selection',
                        title: '知识点',
                        field: 'name',
                        width: 200,
                        align: 'center',
                        formatter: (item) => {
                            return '<a>'+item.name+'</a>'
                        }
                    },
                    {
                        type: 'checkbox',
                        isContainChildren: true, //是否勾选子节点，默认false
                        onChange: this.onCheck, // parmas selectRows
                        width: 200,
                        align: 'center'
                    }
                ],
                lists: [//test
                    {
                    "id":40,
                    "parent_id":0,
                    "order":0,
                    "name":"动物类",
                    "open":true,
                    "lists":[]
                    },{
                    "id":5,
                    "parent_id":0,
                    "order":0,
                    "name":"昆虫类",
                    "open":true,
                    "isShowCheckbox": false,
                    "lists":[
                        {
                        "id":12,
                        "parent_id":5,
                        "open":true,
                        "order":0,
                        "name":"蚂蚁",
                        "uri":"/masd/ds",
                        "lists":[]
                        }
                    ]
                    },
                    {
                    "id":19,
                    "parent_id":0,
                    "order":1,
                    "name":"植物类",
                    "open":true,
                    "lists":[]
                    }
                ],
            }
        };
    },
    methods: {
        onTreeDataChange(list, from, to, where) {
            console.log(from, to, where);
            this.treeData.lists = list;
            console.log(JSON.stringify(list));
        }
    }
}
</script>