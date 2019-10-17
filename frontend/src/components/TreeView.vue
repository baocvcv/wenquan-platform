<template>
    <div class="tree-view">
        <tree :items="testData" v-model="selection"></tree>
    </div>
</template>

<style>
.tree-row:before{
    content: "";
    position: absolute;
    z-index: -1;
    background: #eeeeee;
    border-radius: 10%;
    transform: scaleX(0);
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    transition:transform 0.3s ease-out;
}
.tree-row:hover:before{
    transform: scaleX(2);
}
.tree-row{
    transform: perspective(1px) translateZ(0);
    overflow: hidden;
}
.tree-row:hover{
    background: none !important;
}
</style>

<script>
//import tree from "drag-tree-table"
//https://github.com/mafengwo/vue-drag-tree-table
import tree from "@/components/tree/TreeView";
export default {
    name: "tree-view",
    components: {
        tree
    },
    data: function(){
        return {
            testData: {
                name: "Root",
                children: [
                    {
                        name:"1"
                    },
                    {
                        name:"2"
                    }
                ]
            },
            selection: [],
            treeData: {
                columns: [
                    {
                        type: 'selection',
                        title: '知识点',
                        field: 'name',
                        width: 200,
                        align: 'center',
                        formatter: (item) => {
                            return item.name
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