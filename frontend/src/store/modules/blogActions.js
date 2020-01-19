import _ from "lodash";
import { api } from "@/api/api";

export const actions = {
  fetchBlogCategories({ state, commit }) {
    async function setBlogCategories() {
      commit("SET_LOAD_STAT_BLOG_CATEGORIES", "loading");
      let res = await api("/api/blogcategories/?format=json");

      for (let index = 0; index < res.length; index++) {
        let breadcrumps = [res[index].category];
        let breadcrumpsID = [res[index].id];
        let k = res[index].parent;
        while (k != null) {
          if (k.parent != null) {
            breadcrumps.push(k.category);
            breadcrumpsID.push(k.id);
          } else {
            const parent = res[index].parent;
            let DataParent = res.filter(res => res.id === parent);
            breadcrumps.push(DataParent[0].category);
            breadcrumpsID.push(DataParent[0].id);
          }
          k = k.parent;
        }
        res[index]["breadcrumps"] = breadcrumps.reverse();
        res[index]["breadcrumpsID"] = breadcrumpsID.reverse();
      }

      let orderData = _.orderBy(res, function(o) {
        return o.breadcrumps.join(" ");
      });
      commit("SET_BLOG_CATEGORIES", orderData);
      commit("SET_LOAD_STAT_BLOG_CATEGORIES", "notLoading");
    }

    if (state.blogCategories.length === 0) {
      setBlogCategories();
    }
  },
  fetchBlogPosts({ state, dispatch, commit }) {
    commit("SET_LOAD_STAT_BLOG_POSTS", "loading");
    async function setBlogPosts() {
      let res = await api("/api/blogposts/?format=json");
      _.forEach(res, function(value) {
        if (value.content.length >= 200) {
          value["truncate"] = true;
        }
      });
      commit("SET_BLOG_POSTS", res);
      commit("SET_LOAD_STAT_BLOG_POSTS", "notLoading");
    }

    if (state.blogCategories.length === 0) {
      setBlogPosts();
    }

    _.delay(function() {
      if (
        state.lodStatBlogCategories === "notLoadingBlogCategories" &&
        state.blogCategories.length === 0
      ) {
        dispatch("fetchBlogCategories");
      }
    }, 10);
  }
};