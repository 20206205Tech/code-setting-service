# from fastapi_cache import FastAPICache

# import env


async def clear_persona_cache():
    """Clear all persona cache in Redis"""
    # await FastAPICache.clear(namespace=env.CACHE_NAMESPACE)

    # # 2. XÓA MẠNH TAY: Dùng thẳng client Redis để xóa sạch DB hiện tại (chỉ dùng test môi trường dev)
    # try:
    #     redis_backend = FastAPICache.get_backend()
    #     # Ép xóa toàn bộ dữ liệu trong Redis DB đang trỏ tới
    #     await redis_backend.redis.flushdb()
    #     logger.info("🔥 Đã ép Redis FLUSHDB thành công!")
    # except Exception as e:
    #     logger.error(f"Lỗi khi xóa thẳng Redis: {e}")

    # # return BaseResponse(success=True, message="Đã dọn dẹp Redis sạch sẽ")
