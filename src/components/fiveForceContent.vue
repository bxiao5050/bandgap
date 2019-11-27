<template>
  <div class="five-forse-group">
    <div class="first-second-header-row">
      <div class="first-column">
        <div class="vertical-box"></div>
        <v-touch tag="div" class="normal-yellow-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 0">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="vertical-box"></div>
        <v-touch tag="div" class="normal-green-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 1">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="vertical-box"></div>
        <v-touch tag="div" class="normal-green-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 6">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="vertical-box"></div>
        <v-touch tag="div" class="normal-green-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 7">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
      </div>
      <div class="arrow">
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <!-- <div class="arrow-row">
          <div class="line" v-for="(item, index) in fiveForceData" v-if="index == 1 && item.pointertype_name != '全新用户数'"></div>
        </div> -->
      </div>
      <div class="second-column">
        <div class="vertical-box"></div>
        <div class="normal-arrow-row">
          <div class="arrows">
            <div class="line"></div>
          </div>
        </div>
        <div class="vertical-box"></div>
        <v-touch tag="div" class="normal-yellow-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 3">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="vertical-box"></div>
        <div class="normal-arrow-row">
          <div class="arrows">
            <div class="line"></div>
          </div>
        </div>
        <div class="vertical-box"></div>
        <div class="normal-arrow-row">
          <div class="arrows">
            <div class="line"></div>
          </div>
        </div>
        <!-- <v-touch tag="div" class="normal-yellow-row" v-for="(item, index) in fiveForceData" @tap="openChart(item)" v-if="index == 5">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <v-touch tag="div" class="normal-yellow-row" v-for="(item, index) in fiveForceData" @tap="openChart(item)" v-if="index == 6">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <v-touch tag="div" class="normal-yellow-row" v-for="(item, index) in fiveForceData" @tap="openChart(item)" v-if="index == 7">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="normal-arrow-row">
          <div class="arrows">
            <div class="line"></div>
          </div>
        </div>
        <div class="normal-arrow-row">
          <div class="arrows">
            <div class="line"></div>
          </div>
        </div> -->
      </div>
      <div class="arrow">
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
        <div class="vertical-box"></div>
        <div class="arrow-row">
          <div class="line"></div>
        </div>
      </div>
      <div class="third-column">
        <div class="vertical-box"></div>
        <div class="normal-arrow-corner">
          <div class="box"></div>
        </div>
        <div class="vertical-box"></div>
        <v-touch tag="div" class="normal-green-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 2">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="vertical-box">
          <div class="line"></div>
        </div>
        <v-touch tag="div" class="normal-green-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 4">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="vertical-box">
          <div class="line"></div>
        </div>
        <v-touch tag="div" class="normal-green-row" @tap="openChart(item)" v-for="(item, index) in fiveForceData" v-if="index === 5">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>

        <!-- <v-touch tag="div" class="special-yellow-row" v-for="(item, index) in fiveForceData" @tap="openChart(item)" v-if="index == 8">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="space-30"></div>
        <div class="normal-transparent-row"></div>
        <div class="space-20"></div>
        <v-touch tag="div" class="normal-smallred-row" v-for="(item, index) in fiveForceData" @tap="openChart(item)" v-if="index == 9">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch>
        <div class="space-20"></div>
        <v-touch tag="div" class="normal-red-row" v-for="(item, index) in fiveForceData" @tap="openChart(item)" v-if="index == 10">
          <label class="labs">{{ item["pointertype_name"] || "undefined" }}</label>
          <div class="labs">{{ item[dateArr[7]] || 0 }}</div>
          <div class="labs">
            <div class="fiveforce-trend" :class="{ up: item.trend > 0, down: item.trend < 0 }"></div>
            <span>{{ item["trend"] }}%</span>
          </div>
        </v-touch> -->
      </div>
    </div>
  </div>
</template>
<script>
import commonMethod from "../utils/commonMethod.js";
export default {
  props: ["dateArr"],
  data: function() {
    return {};
  },
  computed: {
    date() {
      return this.dateArr[7];
    },
    indexData: function() {
      return this.$store.state.fiveforcestore.indexData;
    },
    fiveForceData: function() {
      return this.$store.state.fiveforcestore.fiveForceData;
    }
  },
  methods: {
    openChart: function(item) {
      this.$emit("openChart", item);
    }
  }
};
</script>
<style lang="scss">
.fiveforce-trend {
  font-size: 0.5rem;
  font-family: "iconfont" !important;
}

.fiveforce-trend:before {
  content: "\e617";
  color: #f89e54;
}

.fiveforce-trend.up:before {
  font-family: iconfont;
  content: "\e64d";
  color: #2acbcb;
}

.fiveforce-trend.down:before {
  content: "\e60a";
  color: #d87a5d;
}

.five-forse-group {
  padding: 0;
  text-align: center;
  margin-top: 1rem;
  /*background-color: #5F68B9;*/
  .first-second-header-row {
    white-space: nowrap;
    display: flex;
    flex-direction: row;
  }
  .first-column {
    display: flex;
    flex-direction: column;
    width: 2.8rem; //29%;
    height: 12rem; //450px;
  }
  .second-column {
    display: flex;
    flex-direction: column;
    width: 2.8rem; //29%;
    height: 12rem; //450px;
  }
  .third-column {
    display: flex;
    flex-direction: column;
    width: 2.8rem;
    height: 12rem;
    .special-yellow-row {
      width: 100%;
      display: flex;
      align-items: center;
      height: 3.4rem;
      background-color: #ebfae2;
      margin: 0.52rem 0 0 0;
      /*border: 1px solid #C9B626;*/
      text-align: center;
      white-space: normal;
      /*color:#C9B626;*/
      .labs {
        font-size: 12px;
        white-space: nowrap;
        // display: block;
        height: 0.6rem;
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
    .normal-transparent-row {
      width: 100%;
      display: flex;
      align-items: center;
      height: 1.8rem;
      background-color: transparent;
      margin: 0;
      text-align: center;
      white-space: normal;
      .labs {
        font-size: 12px;
        white-space: nowrap;
        // display: block;
        height: 0.6rem;
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
    .normal-smallred-row {
      width: 100%;
      display: flex;
      align-items: center;
      height: 1.8rem;
      background-color: #ffefe7;
      margin: 0;
      /*border: 1px solid #E36031;*/
      text-align: center;
      white-space: normal;
      /*color:#E36031;*/
      .labs {
        font-size: 12px;
        white-space: nowrap;
        // display: block;
        height: 0.6rem;
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
    .normal-red-row {
      width: 100%;
      display: flex;
      align-items: center;
      height: 1.8rem;
      background-color: #ffae88;
      margin: 0;
      /*border: 1px solid #E36031;*/
      text-align: center;
      white-space: normal;
      /*color:#E36031;*/
      .labs {
        font-size: 12px;
        white-space: nowrap;
        // display: block;
        height: 0.6rem;
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
    .space-30 {
      display: block;
      width: 100%;
      height: 0.8rem;
    }
    .space-20 {
      display: block;
      width: 100%;
      height: 0.54rem;
    }
  }
  .vertical-box {
    width: 100%;
    height: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    .line {
      width: 0.1rem;
      height: 0.5rem;
      background: #e0e0e0;
    }
  }
  .arrow {
    display: flex;
    flex-direction: column;
    width: 5%;
    height: 12rem;
    .arrow-row {
      display: flex;
      align-items: center;
      width: 100%;
      height: 1.8rem;
      margin: 0;
      /*color: #E0E0E0;*/
      font-size: 20px;
      .line {
        width: 100%;
        height: 0.1rem;
        background-color: #e0e0e0;
      }
    }
  }
  .normal-green-row {
    width: 100%;
    height: 1.8rem; //70px;
    background-color: #dde7f2;
    margin: 0; // 0.26rem
    /*border: 1px solid #27B78D;*/
    text-align: center;
    white-space: normal;
    display: flex;
    flex-direction: column;
    /*color:#27B78D;*/
    .labs {
      font-size: 12px;
      white-space: nowrap;
      // display: block;
      height: 0.6rem;
      display: -webkit-box;
      -webkit-box-pack: center;
      -webkit-box-align: center;
    }
  }
  .normal-yellow-row {
    width: 100%;
    display: flex;
    flex-direction: column;
    height: 1.8rem; //70px;
    background-color: #ebfae2;
    margin: 0; // 0.26rem
    /*border: 1px solid #C9B626;*/
    text-align: center;
    white-space: normal;
    /*color:#C9B626;*/
    .labs {
      font-size: 12px;
      white-space: nowrap;
      // display: block;
      height: 0.6rem;
      display: -webkit-box;
      -webkit-box-pack: center;
      -webkit-box-align: center;
    }
  }
  .normal-arrow-corner {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 1.8rem;
    margin: 0;
    position: relative;
    .box {
      position: absolute;
      top: 0.85rem;
      left: -1%;
      width: 52%;
      height: 83%;
      border-top: 0.1rem solid #e0e0e0;
      border-right: 0.1rem solid #e0e0e0;
      border-top-right-radius: 0.2rem;
    }
  }
  .normal-arrow-row {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 1.8rem;
    margin: 0;
    .arrows {
      width: 100%;
      height: 0.1rem;
      .line {
        width: 100%;
        height: 0.1rem;
        background-color: #e0e0e0;
      }
    }
  }
}
</style>
