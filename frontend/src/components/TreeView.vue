<template>
    <div class="treeview">
        <tree-view :model="treeData" category="subnodes" :selection="currentSelection" 
        :onSelect="select" :display="display" class="TreeViewDemo" :dragndrop="drag_drop"
        :strategies="strategies" :transition="transition" :openerOpts="openerOpts"/>
        <div>
            <v-btn v-if="editable && !edit" @click="beginEdit" text>Edit</v-btn>
            <v-btn v-if="edit" @click="addSubNode" color="success" small fab class="mx-2 my-2"
                :disabled="currentSelection.length == 0"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn v-if="edit" @click="removeNode" color="error" small fab class="mx-2 my-2"
                :disabled="currentSelection.length == 0"
            >
                <v-icon>mdi-minus</v-icon>
            </v-btn>
            <v-btn v-if="edit" @click="rename" color="primary" small fab class="mx-2 my-2"
                :disabled="currentSelection.length == 0"
            >
                <v-icon>mdi-pencil</v-icon>
            </v-btn>
        </div>
        <v-dialog v-model="renameDialog" persistent max-width="600px">
            <v-card>
                <v-card-title>
                    <span class="headline">Rename</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-text-field v-model="renameName"></v-text-field>
                        <v-btn @click="renameConfirmation" class="mx-2" color="primary"
                            :disabled="renameName == ''"
                        >Confirm</v-btn>
                        <v-btn @click="renameDialog = false" class="mx-2">Cancel</v-btn>
                    </v-container>
                </v-card-text>
            </v-card>
        </v-dialog>
        <v-btn v-if="edit" @click="submit" color="success" class="mx-2 my-2"
            :disabled="treeData.length == 0"
        >Submit</v-btn>
        <v-btn v-if="edit" @click="cancel" color="error" class="mx-2 my-2">Cancel</v-btn>
    </div>
</template>

<script>
import { TreeView } from "@bosket/vue";
import { dragndrop } from "@bosket/core";
import axios from "axios";

export default {
    name: "treeview",
    components: {
        "tree-view": TreeView
    },
    model: {
        prop: "selection",
        event: "selectChange"
    },
    props: {
        editable: {
            type: Boolean,
            default: false
        },
        selection: {
            type: Array,
            default: () => []
        },
        bankID: {
            tyre: Number,
            default: -1
        }
    },
    mounted() {
        this.drag_drop.draggable = false;
        if(this.bankID != -1){
            axios.get("/api/nodes_list/"+ this.bankID + "/")
            .then(response => {
                this.treeData = [response.data];
            })
            .catch(error => {
                this.treeData = [{
                    id: 0,
                    name: error.toString(),
                    subnodes: []
                }];
            });
        }
    },
    computed: {
        currentSelection() {
            //returns the selection in used
            return this.edit ? this.singleSelection : this.selection;
        }
    },
    methods: {
        updateData(data) {
            //load data
            this.treeData = data;
        },
        select(newOne) {
            //a new selection
            if(this.edit) this.singleSelection=newOne
            else this.$emit("selectChange",newOne);
        },
        clearSelection() {
            this.$emit("selectChange",[]);
            this.singleSelection = [];
        },
        beginEdit() {
            //begin edit mode
            this.formerTreeData = JSON.stringify(this.treeData);
            this.edit = true;
            this.singleSelection = [];
            this.deletedID = [];
            this.strategies.selection = ["single"];
            this.drag_drop.draggable = true;
        },
        submit() {
            //submit modification

            //submit changes
            axios.put("/api/nodes_list/" + this.bankID + "/",{
                delete: this.deletedID,
                modify: this.treeData[0]
            })
            .then(response => {
                this.treeData = [response.data];
            })
            .catch(err => console.log(err));

            this.edit = false;
            this.clearSelection();
            this.deletedID = [];
            this.strategies.selection = ["multiple"];
            this.drag_drop.draggable = false;
        },
        cancel() {
            //Cancel Change
            this.treeData = JSON.parse(this.formerTreeData);
            this.edit = false;
            this.clearSelection();
            this.deletedID = [];
            this.strategies.selection = ["multiple"];
            this.drag_drop.draggable = false;
        },
        addSubNode(){
            //add a sub node at selected one
            if(this.currentSelection.length > 0 && this.currentSelection[0].subnodes){
                let newNode={
                    id: -1,
                    name: "No name",
                    subnodes: []
                };
                this.currentSelection[0].subnodes.push(newNode);
            }
        },
        removeNode(){
            //remove the selected node
            if(this.currentSelection.length > 0){
                if(this.currentSelection[0].id != -1){
                    let travelDeleteNode = item => {
                        this.deletedID.push(item.id);
                        if(item.subnodes)
                            item.subnodes.forEach(travelDeleteNode);
                    };
                    travelDeleteNode(this.currentSelection[0]);
                }
                this.currentSelection[0].id=-2;
                let removeFunc=(item,index,arr) => {
                    if(item.id==-2){
                        arr.splice(index,1);
                        return;
                    }
                    if(item.subnodes)
                        item.subnodes.forEach(removeFunc);
                }
                this.treeData.forEach(removeFunc);
                this.singleSelection=[];
            }
        },
        rename(){
            //rename start
            if(this.currentSelection.length > 0){
                this.renameName = this.currentSelection[0].name;
                this.renameDialog = true;
            }
        },
        renameConfirmation(){
            //rename confirm
            this.singleSelection[0].name = this.renameName;
            this.renameDialog = false;
        }
    },
    data: function() {
        return {
            edit: false,
            formerTreeData: "",
            treeData: [{
                id: 0,
                name: "Loading...",
            }],
            singleSelection: [],//used only in edit mode
            deletedID: [],//used only in edit mode
            renameDialog: false,
            renameName: "",

            //tree properties
            drag_drop: { ...dragndrop.selection(() => this.treeData, m => this.treeData = m)},
            strategies: {
                selection: ["multiple"],
                click: ["select", "toggle-fold","unfold-on-selection"],
                fold: ["opener-control"]
            },
            display: item => {
                return item.name;
            },
            transition: {
                attrs: { appear: true },
                props: { name: "TreeViewDemoTransition" }
            },
            openerOpts: {
                position: "right"
            },
        }
    }
}
</script>

<style>
/* Search bar */

.TreeViewDemo>input[type="search"] {
    width: 100%;
    background: rgba(0, 0, 0, 0.05);
    height: 3em;
    border-width: 2px;
    transition: border 0.5s;
}

/* Elements */

.TreeViewDemo {
    box-shadow: 0px 0px 10px #DADADA;
    white-space: nowrap;
}

.TreeViewDemo ul {
    list-style: none;
}

.TreeViewDemo li {
    min-width: 100px;
    transition: all 0.25s ease-in-out;
}

.TreeViewDemo li:hover{
    background-color: #E3F2FD;
}

.TreeViewDemo ul li a {
    color: #222;
}

.TreeViewDemo ul li>.item>a {
    display: inline-block;
    vertical-align: middle;
    width: calc(100% - 55px);
    margin-right: 30px;
    padding: 10px 5px;
    text-decoration: none;
    transition: all 0.25s;
}

.TreeViewDemo ul li:not(.disabled) {
    cursor: pointer;
}

.TreeViewDemo li.selected {
    color:#1565C0;
}

.TreeViewDemo ul li.selected>.item>a {
    color: #1E88E5;
}

.TreeViewDemo ul li.selected>.item>a:hover {
    color: #aaa;
}

.TreeViewDemo ul li:not(.disabled)>.item>a:hover {
    color: #1E88E5;
}


/* Root elements */

.TreeViewDemo ul.depth-0 {
    padding: 20px;
    margin: 0;
    background-color: rgba(255, 255, 255, 0.4);
    user-select: none;
    transition: all 0.25s;
}


/* Categories : Nodes with subnodes */

.TreeViewDemo li.category>.item {
    display: block;
    margin-bottom: 5px;
    transition: all 0.25s ease-in-out;
}

/*
.TreeViewDemo li.category:not(.folded)>.item {
    border-bottom: 1px solid crimson;
}
*/


/* Category opener */

.TreeViewDemo .opener {
    display: inline-block;
    vertical-align: middle;
    font-size: 25px;
    cursor: pointer;
}

.TreeViewDemo .opener::before {
    content: '+';
    display: block;
    transition: all 0.25s;
    font-family: monospace;
}

.TreeViewDemo li.category.async>.item>.opener::before {
    content: '!';
}

.TreeViewDemo .opener:hover {
    color: #1E88E5;
}

.TreeViewDemo li.category:not(.folded)>.item>.opener::before {
    color: #1E88E5;
    transform: rotate(45deg);
}

@keyframes spin {
    from {
        transform: rotate(0deg)
    }
    to {
        transform: rotate(360deg)
    }
}

.TreeViewDemo li.category.loading>.item>.opener::after {
    animation: spin 1s infinite;
}


/* Animations on fold / unfold */

.TreeViewDemoTransition-enter, .TreeViewDemoTransition-leave-to {
    opacity: 0;
    transform: translateX(-50px);
}

.TreeViewDemoTransition-enter-active, .TreeViewDemoTransition-leave-active {
    transition: all .3s ease-in-out;
}


/* Drag'n'drop */

.TreeViewDemo li.dragover, .TreeViewDemo ul.dragover {
    box-shadow: 0px 0px 5px #CCC
}

.TreeViewDemo ul.dragover {
    background-color: rgba(200, 200, 200, 0.3);
}

.TreeViewDemo li.dragover {
    background-color: rgba(100, 100, 100, 0.05);
    padding: 0px 5px;
}

.TreeViewDemo li.dragover>span.item {
    border-color: transparent;
}

.TreeViewDemo li.nodrop {
    box-shadow: 0px 0px 5px crimson;
    background-color: rgba(255, 20, 60, 0.1);
    padding: 0px 5px;
}

</style>