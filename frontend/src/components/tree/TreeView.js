import Tree from "./TreeView";
import VCheckBox from "vuetify/lib/components/VCheckbox/VCheckbox";

export default {
  name: "tree-view",

  props: {
    captionField: {
      type: String,
      required: false,
      default: "name"
    },
    childrenField: {
      type: String,
      required: false,
      default: "children"
    },
    items: {
      type: Object,
      required: true,
      default: () => {}
    },
    value: {
      type: Array,
      required: false,
      default: null
    }
  },

  computed: {
    caption() {
      return this.items[this.captionField];
    },
    hasChildren() {
      return (
        !!this.items[this.childrenField] &&
        this.items[this.childrenField].length > 0
      );
    },
    hasSelection() {
      return !!this.value && this.value.length > 0;
    },
    allLeafs() {
      let leafs = [];
      let searchTree = items => {
        if (
          !!items[this.childrenField] &&
          items[this.childrenField].length > 0
        ) {
          items[this.childrenField].forEach(child => searchTree(child));
        } else {
          leafs.push(items);
        }
      };
      searchTree(this.items);
      return leafs;
    },
    allLeafsSelected() {
      return (
        this.hasChildren &&
        this.hasSelection &&
        this.allLeafs.every(leaf =>
          this.value.some(leafItem => leafItem === leaf)
        )
      );
    },
    someLeafsSelected() {
      return (
        this.hasChildren &&
        this.hasSelection &&
        this.allLeafs.some(leaf =>
          this.value.some(leafItem => leafItem === leaf)
        )
      );
    },
    indeterminate() {
      return (
        this.hasChildren &&
        this.hasSelection &&
        this.someLeafsSelected &&
        !this.allLeafsSelected
      );
    }
  },

  methods: {
    genChild(child) {
      return this.$createElement(Tree, {
        class: "ml-4",
        props: {
          captionField: this.captionField,
          childrenField: this.childrenField,
          items: child,
          value: this.value
        },
        on: {
          input: selection => {
            this.$emit("input", selection);
          }
        }
      });
    },
    genChildren() {
      let childrenList = [];
      if (this.items[this.childrenField]) {
        this.items[this.childrenField].forEach(element => {
          childrenList.push(this.genChild(element));
        });
      }
      return childrenList;
    },
    genRoot() {
      if (this.value) {
        return this.$createElement(VCheckBox, {
          props: {
            label: this.caption,
            hideDetails: true,
            inputValue: this.hasChildren ? [true] : this.value,
            value: this.hasChildren ? this.allLeafsSelected : this.items,
            indeterminate: this.indeterminate
          },
          on: {
            change: selection => {
              if (this.hasChildren) {
                if (this.allLeafsSelected) {
                  this.allLeafs.forEach(leaf => {
                    let index = this.value.indexOf(leaf);
                    this.value.splice(index, 1);
                  });
                } else {
                  this.allLeafs.forEach(leaf => {
                    let index = this.value.indexOf(leaf);
                    if (index === -1) {
                      this.value.push(leaf);
                    }
                  });
                }
                this.$emit("input", this.value);
              } else this.$emit("input", selection);
            }
          }
        });
      } else {
        return this.$createElement(
          "div",
          {
            class: [
              "input-group",
              "check-box",
              "input-group--hide-details",
              "input-group--selection-controls",
              "accent-text"
            ]
          },
          [
            this.$createElement(
              "label",
              {
                class: "treeview-label"
              },
              [this.caption]
            )
          ]
        );
      }
    }
  },

  render(createElement) {
    return createElement("div", {}, [this.genRoot(), ...this.genChildren()]);
  }
};
