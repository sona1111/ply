import { AbstractDashboardApp } from "/static/dashboard/js/Dashboard/AbstractDashboardApp.js";
import { SmartSelect } from "/static/core.plyui/js/SmartSelect/SmartSelect.js";
export class GalleryUserCollections extends AbstractDashboardApp {

        close_manager(ev) {
           ev.preventDefault();
           ev.stopPropagation();
           this._hideModal();
        }
        show_manager(ev) {
           this._getModal();
           ev.preventDefault();
           ev.stopPropagation();
           this._showModal();
        }
        constructor(name) {
            super(name);
            this.urls = {
                "submit":"media.gallery.core/api/collections/create"
            }


            this.elements = {
                "form":"#collections_form",
                "modal":"#collectionManagerModal",

            }

            console.info("Gallery User Collections Manager Ready.")

        }
 }