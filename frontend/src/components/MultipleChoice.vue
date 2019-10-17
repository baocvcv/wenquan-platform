<template>
    <div class="multiple-choice-component">
        <v-form ref="multi-choice-form" v-model="valid">
            <v-text-field label="Title" v-model="title" outlined></v-text-field>
            <v-textarea 
                label="Content"
                v-model="content" 
                outlined
                auto-grow
            ></v-textarea>
            <v-list>
                <v-list-item-group>
                    <v-list-item
                        v-for="(item,index) in choices"
                        :key="item.name"
                    >
                        <v-list-item-icon @click="changeRightStatus(item)">
                            <span v-if="item.right">
                                [ {{ item.name }} ]
                            </span>
                            <span v-else>
                                {{ item.name }}
                            </span>
                        </v-list-item-icon>
                        <v-text-field
                            placeholder="Enter choice"
                            v-model="item.content"
                        ></v-text-field>
                        <v-btn icon small
                            @click="removeChoice(index)">
                            <v-icon>mdi-minus</v-icon>
                        </v-btn>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
            <v-btn
                class="mx-2"
                fab
                dark
                color="indigo"
                @click="addChoice()"
            >
                <v-icon dark>mdi-plus</v-icon>
            </v-btn>
        </v-form>
    </div>
</template>

<script>
export default {
    name: "multiple-choice",
    props: {
        title: {
            type: String,
            default: "",
        },
        content: {
            type: String,
            default: "",
        },
        choices: {
            type: Array,
            default: () => [
            {
                name: "A",
                content: "",
                right: false
            },
            {
                name: "B",
                content: "",
                right: false
            },
            {
                name: "C",
                content: "",
                right: false
            },
            {
                name: "D",
                content: "",
                right: false
            },
            ],
        },
        rightAnswer: {
            type: Array,
            default: () => [],
        },
    },
    methods: {
        addChoice() {
            let length=this.choices.length;
            this.choices.push({
                name: String.fromCharCode(65+length),
                content: ""
            });
        },
        removeChoice(index) {
            if(this.choices[index].right)
                this.rightAnswer.splice(this.rightAnswer.indexOf(this.choices[index]));
            this.choices.splice(index,1);
            for(var i=0;i<this.choices.length;i++)
                this.choices[i].name=String.fromCharCode(65+i);
        },
        changeRightStatus(item) {
            item.right=!item.right;
            if(item.right) this.rightAnswer.push(item);
            else this.rightAnswer.splice(this.rightAnswer.indexOf(item),1);
            console.log(JSON.stringify(this.rightAnswer))
        }
    },
    data: function() {
        return {
            valid: false,
        };
    }
}
</script>