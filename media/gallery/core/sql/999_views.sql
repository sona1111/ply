DROP VIEW IF EXISTS media_gallery_core_collection_permission_view;
CREATE OR REPLACE VIEW media_gallery_core_collection_permission_view AS  SELECT DISTINCT
    media_gallery_core_collection_permission.id AS gcp_id,
    media_gallery_core_collection_permission.updated AS gcp_updated,
    media_gallery_core_collection_permission.owner AS gcp_owner,
    media_gallery_core_collection_permission.archived AS gcp_archived,
    media_gallery_core_collection_permission.public AS gcp_public,
    media_gallery_core_collection_permission.searchable AS gcp_searchable,
    media_gallery_core_collection_permission.shareable AS gcp_shareable,
    media_gallery_core_collection_permission."create" AS gcp_create,
    media_gallery_core_collection_permission.edit AS gcp_edit,
    media_gallery_core_collection_permission.delete AS gcp_delete,
    media_gallery_core_collection_permission.nsfw AS gcp_nsfw,
    media_gallery_core_collection_permission.explicit AS gcp_explicit,
    media_gallery_core_collection_permission.comment AS gcp_comment,
    media_gallery_core_collection_permission.profile_id AS gcp_profile,
    media_gallery_core_collection_permission.community_id AS gcp_community,
    media_gallery_core_collection.collection_id AS gc_id,
    media_gallery_core_collection.label AS gc_label,
    media_gallery_core_collection.created AS gc_created,
    media_gallery_core_collection.updated AS gc_updated,
    media_gallery_core_collection.items AS gc_items,
    media_gallery_core_collection.views AS gc_views,
    media_gallery_core_collection.likes AS gc_likes,
    media_gallery_core_collection.shares AS gc_shares,
    media_gallery_core_collection.comments AS gc_comments,
    media_gallery_core_collection.uuid AS gc_uuid,
    media_gallery_core_collection_items."order" AS gci_order,
    media_gallery_core_item.item_hash AS gci_hash,
    media_gallery_core_item.title AS gci_title,
    media_gallery_core_item.descr AS gci_descr,
    media_gallery_core_item.created AS gci_created,
    media_gallery_core_item.updated AS gci_updated,
    media_gallery_core_item.files AS gci_files,
    media_gallery_core_item.views AS gci_views,
    media_gallery_core_item.likes AS gci_likes,
    media_gallery_core_item.shares AS gci_shares,
    media_gallery_core_item.comments AS gci_comments,
    media_gallery_core_item.nsfw AS gci_nsfw,
    media_gallery_core_item.plugin AS gci_plugin,
    media_gallery_core_item.plugin_data AS gci_plugin_data,
    media_gallery_core_item.thumbnail AS gci_thumbnail,
    media_gallery_core_item.processed AS gci_processed,
    media_gallery_core_item.uuid AS gci_uuid,
    media_gallery_core_item.configured AS gci_configured,
    media_gallery_core_item.active AS gci_active,
    media_gallery_core_item.archived AS gci_archived,
    media_gallery_core_item.frozen AS gci_frozen,
    media_gallery_core_item.hidden AS gci_hidden,
    media_gallery_core_item.downloads AS gci_downloads,
    media_gallery_core_item.profile_id AS gci_profile,
    media_gallery_core_item.details AS gci_details,
    media_gallery_core_item.sizing AS gci_sizing,
    media_gallery_core_item.style AS gci_style,
    media_gallery_core_item.rating AS gci_rating,
    media_gallery_core_item_file.name AS gif_name,
    media_gallery_core_item_file.hash AS gif_hash,
    media_gallery_core_item_file.id AS gif_id,
    media_gallery_core_item_file.data AS gif_data,
    media_gallery_core_item_file.created AS gif_created,
    media_gallery_core_item_file.updated AS gif_updated,
    media_gallery_core_item_file.meta AS gif_meta,
    media_gallery_core_item_file.bindata AS gif_bindata,
    media_gallery_core_item_file.jsondata AS gif_jsondata,
    media_gallery_core_item_file.thumbnail AS gif_thumbnail,
    media_gallery_core_item_file.file_size AS gif_size,
    media_gallery_core_item_file.type AS gif_type,
    media_gallery_core_item_file.original AS gif_original,
    media_gallery_core_item_file.item_id AS gif_item,
    media_gallery_core_collection_permission.id AS id,
    media_gallery_core_collection.uuid AS collection_id,
    media_gallery_core_collection_permission.community_id AS community_id,
    media_gallery_core_item_file.id as file_id,
    media_gallery_core_item.uuid as item_id,
    communities_profiles_profile.name as profile_name,
    communities_profiles_profile.pronouns as profile_pronouns,
    communities_profiles_profile.avatar as profile_avatar,
    communities_profiles_profile.slug as profile_slug,
    communities_profiles_profile.uuid as profile_uuid,
    communities_profiles_profile.uuid as profile_id
   FROM media_gallery_core_collection_permission
     JOIN media_gallery_core_collection ON media_gallery_core_collection_permission.collection_id = media_gallery_core_collection.uuid
     JOIN media_gallery_core_collection_items ON media_gallery_core_collection.uuid = media_gallery_core_collection_items.collection_id
     JOIN media_gallery_core_item ON media_gallery_core_collection_items.item_id = media_gallery_core_item.uuid
     JOIN media_gallery_core_item_file ON media_gallery_core_item.uuid = media_gallery_core_item_file.item_id
     JOIN communities_profiles_profile ON communities_profiles_profile.uuid = media_gallery_core_collection_permission.profile_id
   WHERE media_gallery_core_item_file.name != ''
   ORDER BY gif_created DESC;  
   
CREATE RULE media_gallery_core_collection_permission_view_delete_rule
AS ON DELETE TO media_gallery_core_collection_permission_view
DO INSTEAD NOTHING;



DROP VIEW IF EXISTS "gallery_itemsbyfavouriteview";
CREATE OR REPLACE VIEW "gallery_itemsbyfavouriteview" AS
SELECT DISTINCT ON (media_gallery_core_item_file.hash) hash as gci_hash,
    media_gallery_core_favourite.profile_id AS gif_profile,
    media_gallery_core_item.title AS gci_title,
    media_gallery_core_item.descr AS gci_descr,
    media_gallery_core_item.created AS gci_created,
    media_gallery_core_item.updated AS gci_updated,
    media_gallery_core_item.files AS gci_files,
    media_gallery_core_item.views AS gci_views,
    media_gallery_core_item.likes AS gci_likes,
    media_gallery_core_item.shares AS gci_shares,
    media_gallery_core_item.comments AS gci_comments,
    media_gallery_core_item.nsfw AS gci_nsfw,
    media_gallery_core_item.plugin AS gci_plugin,
    media_gallery_core_item.plugin_data AS gci_plugin_data,
    media_gallery_core_item.thumbnail AS gci_thumbnail,
    media_gallery_core_item.processed AS gci_processed,
    media_gallery_core_item.uuid AS gci_uuid,
    media_gallery_core_item.configured AS gci_configured,
    media_gallery_core_item.active AS gci_active,
    media_gallery_core_item.archived AS gci_archived,
    media_gallery_core_item.frozen AS gci_frozen,
    media_gallery_core_item.hidden AS gci_hidden,
    media_gallery_core_item.downloads AS gci_downloads,
    media_gallery_core_item.profile_id AS gci_profile,
    media_gallery_core_item.details AS gci_details,
    media_gallery_core_item.sizing AS gci_sizing,
    media_gallery_core_item.style AS gci_style,
    media_gallery_core_item.rating AS gci_rating,
    media_gallery_core_item_file.name AS gif_name,
    media_gallery_core_item_file.id AS gif_id,
    media_gallery_core_item_file.data AS gif_data,
    media_gallery_core_item_file.created AS gif_created,
    media_gallery_core_item_file.updated AS gif_updated,
    media_gallery_core_item_file.meta AS gif_meta,
    media_gallery_core_item_file.bindata AS gif_bindata,
    media_gallery_core_item_file.jsondata AS gif_jsondata,
    media_gallery_core_item_file.thumbnail AS gif_thumbnail,
    media_gallery_core_item_file.file_size AS gif_size,
    media_gallery_core_item_file.type AS gif_type,
    media_gallery_core_item_file.original AS gif_original,
    media_gallery_core_item_file.item_id AS gif_item,
    media_gallery_core_item_file.id AS file_id,
    media_gallery_core_item.uuid AS item_id,
    communities_profiles_profile.name AS profile_name,
    communities_profiles_profile.pronouns AS profile_pronouns,
    communities_profiles_profile.avatar AS profile_avatar,
    communities_profiles_profile.slug AS profile_slug,
    communities_profiles_profile.uuid AS profile_uuid,
    communities_profiles_profile.uuid AS profile_id,
    media_gallery_core_favourite.id AS id,
    substring(communities_profiles_profile.uuid::text from 1 for 1)||'/'||substring(communities_profiles_profile.uuid::text from 2 for 1)||'/'||substring(communities_profiles_profile.uuid::text from 3 for 1) AS gal_path,
    UUID('0011aa22-bb33-0001-0001-bb330011aa22') AS gc_uuid,
    UUID('0011aa22-bb33-0001-0001-bb330011aa22') AS gc_id,
    UUID('0011aa22-bb33-0001-0001-bb330011aa22') AS collection_id
    FROM media_gallery_core_favourite
     JOIN media_gallery_core_item ON media_gallery_core_favourite.item_id = media_gallery_core_item.uuid
     JOIN media_gallery_core_item_file ON media_gallery_core_item.uuid = media_gallery_core_item_file.item_id
     JOIN communities_profiles_profile ON communities_profiles_profile.uuid = media_gallery_core_item.profile_id
  WHERE media_gallery_core_item_file.name <> ''::text  AND media_gallery_core_item_file.thumbnail = true;
