<template>
    <div class="treeview">
        <tree-view :model="testData" category="subnodes" :selection="selection" 
        :onSelect="select" :display="display" class="TreeViewDemo" :dragndrop="d"
        :strategies="strategies" :transition="transition" :openerOpts="openerOpts"/>
        {{ selection }}
        <br/>
        {{ testData }}
        <v-btn v-if="edit" @click="submit">Submit</v-btn>
    </div>
</template>

<script>
import { TreeView } from "@bosket/vue"
import { dragndrop } from "@bosket/core"
export default {
    name: "treeview",
    components: {
        "tree-view": TreeView
    },
    props: {
        treeData: {
            type: Object,
            default: () => {}
        },
        edit: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        select(newOne) {
            this.selection=newOne
            if(!this.edit) this.$emit("selectChange",newOne);
        },
        submit() {
            this.$emit("treeSubmit",treeData);
        }
    },
    data: function() {
        return {
            d: { ...dragndrop.selection(() => this.testData, m => this.testData = m)},
            strategies: {
                selection: ["multiple"],
                click: ["select", "toggle-fold"],
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
            testData: [
                    { name: "Click me, I'm a node with two subnodes.", subnodes: [
                        { name: "I am a childless leaf." },
                        { name: "I am a also a childless leaf." }
                    ]},
                    { name: "I'm a leaf, I do not have subnodes.",subnodes:[] },
                    { name: "I am an asynchronous node, click me and wait one second."}
                ],
            selection: [],
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