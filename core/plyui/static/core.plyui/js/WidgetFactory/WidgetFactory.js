export class WidgetFactory {

    hideEl(el) {
        $(el).removeClass('animate__fadeIn');
        $(el).addClass('animate__animated animate__fadeOut');
    }
    fadeInEl(el) {
        $(el).removeClass('animate__fadeOut');
        $(el).addClass('animate__animated animate__fadeIn');
    }

    create_block(className,id,html,cssClass) {
        var blk = $("<"+className+">",{id:id,class:cssClass,html:html});
        return blk;
    }
    create_icon(className) {
        var icon = "<i class=\""+className+"\"></i>";
        return icon
    }
    set_progressbar(pbar,value) {
        var elf = $(pbar).find(".progress-bar");
        elf.css('width',value+'%');
        elf.text(value+'%');
    }
    create_img(id,src,alt,className) {
        var image = $("<img>",{id:id,src:src,alt:alt,class:className});
        return image
    }
    create_progressbar(idpfx,max,current,className,selector_data) {
        var pbarc = $("<div>",{id:"container_progress_"+idpfx,class:'progress'});
        var curr = (current/max)*100;
        var pbar = $("<div>",{id:"progress_"+idpfx,class:'progress-bar progress-bar-striped progress-bar-animated '+className,role:'progressbar','text':curr+"%"});
        pbar.css('width',curr+"%");
        pbarc.append(pbar);
        if (selector_data !== undefined) {
            pbar.addClass('_fs-'+selector_data);
        }

        return pbarc;
    }
    create_generic_card(prefix,index,icon,header,text,className) {
        var card = $("<div>",{id:prefix+index,class:className});
        var icon = $("<div>",{id:"icon"+index,class:"card-img-top",html:icon});
        var header = $("<div>",{id:"header_"+index,class:"card-header",text:header});
        var text = $("<div>",{id:"text_"+index,class:"card-text",html:text});
        card.append(header,text);
        header.append(icon);
        return card;
    }

    constructor() {

    }

}
 console.info("Dashboard Widget Factory Loaded.")
// <div className="progress"> <div className="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div></div>